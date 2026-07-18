#!/usr/bin/env python3
"""Registru YAML pentru persoanele analizate numerologic."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - depinde de mediul local
    raise SystemExit(
        "Lipsește PyYAML. Rulează: python -m pip install -r "
        "skills/numerologie-gestionare-persoane/requirements.txt"
    ) from exc


SCHEMA_VERSION = 1


def find_atlas_root() -> Path:
    configured = os.environ.get("ATLAS_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    current = Path.cwd().resolve()
    for candidate in (current, *current.parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "skills").is_dir():
            return candidate
    return current


ATLAS_ROOT = find_atlas_root()
DEFAULT_REGISTRY = ATLAS_ROOT / "persoane"
GENDERS = {"masculin", "feminin"}
EXPRESSIONS = {"conversational", "formal"}
DETAIL_LEVELS = {"scurt", "mediu", "amplu"}
INTERVAL_TYPES = {"complet", "specific"}
RELATION_STATUSES = {"confirmata", "provizorie"}


class ValidationError(ValueError):
    """Datele persoanei nu respectă schema."""


def fail(message: str) -> None:
    raise ValidationError(message)


def clean_text(value: Any, field: str, *, required: bool = True) -> str:
    if value is None:
        value = ""
    text = " ".join(str(value).strip().split())
    if required and not text:
        fail(f"Câmpul {field} este obligatoriu.")
    return text


def iso_date(value: Any, field: str, *, required: bool = True) -> str | None:
    if value in (None, ""):
        if required:
            fail(f"Câmpul {field} este obligatoriu.")
        return None
    if isinstance(value, datetime):
        parsed = value.date()
    elif isinstance(value, date):
        parsed = value
    else:
        raw = str(value).strip()
        parsed = None
        for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d-%m-%Y"):
            try:
                parsed = datetime.strptime(raw, fmt).date()
                break
            except ValueError:
                continue
        if parsed is None:
            fail(f"{field} trebuie să fie o dată validă ZZ.LL.AAAA sau YYYY-MM-DD.")
    if field.endswith("data_nasterii") and parsed > date.today():
        fail(f"{field} nu poate fi în viitor.")
    return parsed.isoformat()


def optional_birth_time(value: Any, field: str = "identitate.ora_nasterii") -> str | None:
    if value in (None, ""):
        return None
    raw = str(value).strip()
    if not re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", raw):
        fail(f"{field} trebuie să fie o oră validă în format HH:MM sau null.")
    return raw


def person_id(birth_date: Any, full_name: Any) -> str:
    birth = iso_date(birth_date, "identitate.data_nasterii")
    name = clean_text(full_name, "identitate.nume_complet")
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_name).strip("-").upper()
    if not slug:
        fail("Numele complet nu poate genera un identificator valid.")
    return f"{birth}-{slug}"


def string_list(value: Any, field: str) -> list[str]:
    if value in (None, ""):
        return []
    if not isinstance(value, list):
        fail(f"{field} trebuie să fie o listă.")
    return [clean_text(item, field) for item in value]


def integer(value: Any, field: str) -> int:
    if isinstance(value, bool):
        fail(f"{field} trebuie să fie număr întreg.")
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        fail(f"{field} trebuie să fie număr întreg.")
    return parsed


def normalize_questions(value: Any) -> list[dict[str, str]]:
    if value in (None, ""):
        return []
    if not isinstance(value, list):
        fail("intrebari trebuie să fie o listă.")
    result = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(f"intrebari[{index}] trebuie să fie obiect.")
        result.append(
            {
                "categorie": clean_text(item.get("categorie"), f"intrebari[{index}].categorie"),
                "text": clean_text(item.get("text"), f"intrebari[{index}].text"),
            }
        )
    return result


def normalize_relations(value: Any, registry: Path) -> list[dict[str, Any]]:
    if value in (None, ""):
        return []
    if not isinstance(value, list):
        fail("relatii trebuie să fie o listă.")
    result = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(f"relatii[{index}] trebuie să fie obiect.")
        linked_id = clean_text(item.get("persoana_id"), f"relatii[{index}].persoana_id", required=False) or None
        status = clean_text(item.get("status") or "provizorie", f"relatii[{index}].status")
        if status not in RELATION_STATUSES:
            fail(f"relatii[{index}].status trebuie să fie confirmata sau provizorie.")
        if status == "confirmata":
            if not linked_id:
                fail(f"relatii[{index}] confirmată necesită persoana_id.")
            if not (registry / linked_id / "persoana.yaml").is_file():
                fail(f"relatii[{index}].persoana_id nu există în registru.")
        result.append(
            {
                "persoana_id": linked_id,
                "nume": clean_text(item.get("nume"), f"relatii[{index}].nume"),
                "data_nasterii": iso_date(
                    item.get("data_nasterii"), f"relatii[{index}].data_nasterii", required=False
                ),
                "tip": clean_text(item.get("tip"), f"relatii[{index}].tip"),
                "status": status,
            }
        )
    return result


def normalize_profile(raw: Any, registry: Path) -> dict[str, Any]:
    if not isinstance(raw, dict):
        fail("Fișa trebuie să conțină un obiect YAML/JSON.")
    supplied_version = raw.get("schema_version", SCHEMA_VERSION)
    if supplied_version != SCHEMA_VERSION:
        fail(f"schema_version trebuie să fie {SCHEMA_VERSION}.")
    identity = raw.get("identitate")
    if not isinstance(identity, dict):
        fail("Secțiunea identitate este obligatorie.")

    full_name = clean_text(identity.get("nume_complet"), "identitate.nume_complet")
    birth_date = iso_date(identity.get("data_nasterii"), "identitate.data_nasterii")
    generated_id = person_id(birth_date, full_name)
    supplied_id = clean_text(raw.get("id"), "id", required=False)
    if supplied_id and supplied_id != generated_id:
        fail(f"id trebuie să fie {generated_id}.")

    gender = clean_text(identity.get("gen"), "identitate.gen").lower()
    if gender not in GENDERS:
        fail("identitate.gen trebuie să fie masculin sau feminin.")

    preferences = raw.get("preferinte_lucrare") or {}
    if not isinstance(preferences, dict):
        fail("preferinte_lucrare trebuie să fie obiect.")
    expression = clean_text(preferences.get("exprimare") or "conversational", "preferinte_lucrare.exprimare")
    detail = clean_text(preferences.get("nivel_detaliere") or "amplu", "preferinte_lucrare.nivel_detaliere")
    if expression not in EXPRESSIONS:
        fail("preferinte_lucrare.exprimare trebuie să fie conversational sau formal.")
    if detail not in DETAIL_LEVELS:
        fail("preferinte_lucrare.nivel_detaliere trebuie să fie scurt, mediu sau amplu.")

    interval = preferences.get("interval_ani") or {}
    if not isinstance(interval, dict):
        fail("preferinte_lucrare.interval_ani trebuie să fie obiect.")
    interval_type = clean_text(interval.get("tip") or "complet", "preferinte_lucrare.interval_ani.tip")
    if interval_type not in INTERVAL_TYPES:
        fail("Tipul intervalului trebuie să fie complet sau specific.")
    start_age = integer(interval.get("start_varsta", 0), "preferinte_lucrare.interval_ani.start_varsta")
    end_age = integer(interval.get("final_varsta", 108), "preferinte_lucrare.interval_ani.final_varsta")
    if interval_type == "complet":
        start_age, end_age = 0, 108
    if not (0 <= start_age <= end_age <= 108):
        fail("Intervalul de vârstă trebuie să fie între 0 și 108, în ordine crescătoare.")

    metadata = raw.get("metadata") or {}
    if not isinstance(metadata, dict):
        fail("metadata trebuie să fie obiect.")
    created = clean_text(metadata.get("created_at"), "metadata.created_at", required=False) or None
    updated = clean_text(metadata.get("updated_at"), "metadata.updated_at", required=False) or None

    return {
        "schema_version": SCHEMA_VERSION,
        "id": generated_id,
        "identitate": {
            "nume_complet": full_name,
            "nume_familie": clean_text(identity.get("nume_familie"), "identitate.nume_familie"),
            "prenume": clean_text(identity.get("prenume"), "identitate.prenume"),
            "prenume_activ": clean_text(identity.get("prenume_activ"), "identitate.prenume_activ"),
            "data_nasterii": birth_date,
            "ora_nasterii": optional_birth_time(identity.get("ora_nasterii")),
            "gen": gender,
            "nume_anterioare": string_list(identity.get("nume_anterioare"), "identitate.nume_anterioare"),
        },
        "preferinte_lucrare": {
            "template": clean_text(preferences.get("template") or "examen", "preferinte_lucrare.template"),
            "exprimare": expression,
            "nivel_detaliere": detail,
            "interval_ani": {
                "tip": interval_type,
                "start_varsta": start_age,
                "final_varsta": end_age,
            },
        },
        "intrebari": normalize_questions(raw.get("intrebari")),
        "relatii": normalize_relations(raw.get("relatii"), registry),
        "metadata": {
            "created_at": created,
            "updated_at": updated,
        },
    }


def load_document(path: Path) -> Any:
    if not path.is_file():
        fail(f"Fișierul nu există: {path}")
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            return json.load(handle)
        return yaml.safe_load(handle)


def write_document(path: Path, profile: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        yaml.safe_dump(profile, handle, allow_unicode=True, sort_keys=False, default_flow_style=False)


def command_save(args: argparse.Namespace) -> int:
    if not args.confirmat:
        fail("Salvarea necesită confirmarea explicită și opțiunea --confirmat.")
    registry = args.root.resolve()
    raw = load_document(args.input.resolve())
    profile = normalize_profile(raw, registry)
    target = registry / profile["id"] / "persoana.yaml"
    existing = None
    if target.exists():
        if not args.actualizare:
            fail(f"Persoana există deja: {profile['id']}. Folosește --actualizare după confirmare.")
        existing = normalize_profile(load_document(target), registry)
    elif args.actualizare:
        fail(f"Persoana nu există și nu poate fi actualizată: {profile['id']}.")

    now = datetime.now().astimezone().isoformat(timespec="seconds")
    profile["metadata"]["created_at"] = (
        existing["metadata"]["created_at"] if existing else profile["metadata"]["created_at"] or now
    )
    profile["metadata"]["updated_at"] = now
    write_document(target, profile)
    print(target)
    return 0


def command_validate(args: argparse.Namespace) -> int:
    profile = normalize_profile(load_document(args.path.resolve()), args.root.resolve())
    print(f"VALID: {profile['id']}")
    return 0


def command_show(args: argparse.Namespace) -> int:
    path = args.root.resolve() / args.id / "persoana.yaml"
    profile = normalize_profile(load_document(path), args.root.resolve())
    print(yaml.safe_dump(profile, allow_unicode=True, sort_keys=False).rstrip())
    return 0


def command_list(args: argparse.Namespace) -> int:
    registry = args.root.resolve()
    rows = []
    if registry.exists():
        for path in sorted(registry.glob("*/persoana.yaml")):
            profile = normalize_profile(load_document(path), registry)
            rows.append(
                {
                    "id": profile["id"],
                    "nume_complet": profile["identitate"]["nume_complet"],
                    "data_nasterii": profile["identitate"]["data_nasterii"],
                }
            )
    print(yaml.safe_dump(rows, allow_unicode=True, sort_keys=False).rstrip() if rows else "[]")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.set_defaults(root=DEFAULT_REGISTRY)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build-id", help="Generează identificatorul canonic.")
    build.add_argument("--data-nasterii", required=True)
    build.add_argument("--nume-complet", required=True)
    build.set_defaults(handler=lambda args: print(person_id(args.data_nasterii, args.nume_complet)) or 0)

    save = subparsers.add_parser("save", help="Validează și salvează o fișă confirmată.")
    save.add_argument("--input", type=Path, required=True)
    save.add_argument("--root", type=Path, default=DEFAULT_REGISTRY)
    save.add_argument("--confirmat", action="store_true")
    save.add_argument("--actualizare", action="store_true")
    save.set_defaults(handler=command_save)

    validate = subparsers.add_parser("validate", help="Validează o fișă existentă.")
    validate.add_argument("path", type=Path)
    validate.add_argument("--root", type=Path, default=DEFAULT_REGISTRY)
    validate.set_defaults(handler=command_validate)

    show = subparsers.add_parser("show", help="Afișează fișa unei persoane.")
    show.add_argument("id")
    show.add_argument("--root", type=Path, default=DEFAULT_REGISTRY)
    show.set_defaults(handler=command_show)

    list_people = subparsers.add_parser("list", help="Listează persoanele din registru.")
    list_people.add_argument("--root", type=Path, default=DEFAULT_REGISTRY)
    list_people.set_defaults(handler=command_list)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.handler(args)
    except (ValidationError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"EROARE: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
