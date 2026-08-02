from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date, datetime
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parent
PERSONS_DIR = ROOT / "persoane"
MAX_BODY_BYTES = 512_000


def ascii_slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").upper()
    return re.sub(r"[^A-Z0-9]+", "-", ascii_value).strip("-")


def require_text(value: object, field: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"Câmpul {field} este obligatoriu.")
    return text


def validate_iso_date(value: object, field: str = "data_nasterii") -> str:
    text = require_text(value, field)
    try:
        parsed = date.fromisoformat(text)
    except ValueError as error:
        raise ValueError(f"Câmpul {field} trebuie să fie o dată ISO validă.") from error
    if parsed > date.today():
        raise ValueError(f"Câmpul {field} nu poate fi în viitor.")
    return text


def normalize_document(payload: dict, now: datetime) -> dict:
    identity = payload.get("identitate") or {}
    full_name = require_text(identity.get("nume_complet"), "nume_complet")
    birth_date = validate_iso_date(identity.get("data_nasterii"))
    gender = require_text(identity.get("gen"), "gen")
    if gender not in {"masculin", "feminin"}:
        raise ValueError("Genul trebuie să fie masculin sau feminin.")

    birth_time = identity.get("ora_nasterii")
    if birth_time in {"", None}:
        birth_time = None
    elif not re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", str(birth_time)):
        raise ValueError("Ora nașterii trebuie să fie HH:MM sau necompletată.")

    relations = []
    for relation in payload.get("relatii") or []:
        relation_name = require_text(relation.get("nume"), "relație.nume")
        relation_date = validate_iso_date(relation.get("data_nasterii"), "relație.data_nasterii")
        relation_gender = require_text(relation.get("gen"), "relație.gen")
        if relation_gender not in {"masculin", "feminin"}:
            raise ValueError("Genul persoanei asociate trebuie să fie masculin sau feminin.")
        relations.append({
            "persoana_id": relation.get("persoana_id"),
            "nume": relation_name,
            "data_nasterii": relation_date,
            "gen": relation_gender,
            "tip": require_text(relation.get("tip"), "relație.tip"),
            "status": relation.get("status") if relation.get("status") in {"confirmata", "provizorie"} else "provizorie",
        })

    questions = []
    for question in payload.get("intrebari") or []:
        text = str(question.get("text") or "").strip()
        if text:
            questions.append({"categorie": require_text(question.get("categorie"), "întrebare.categorie"), "text": text})

    preferences = payload.get("preferinte_lucrare") or {}
    interval = preferences.get("interval_ani") or {}
    interval_type = interval.get("tip") if interval.get("tip") in {"complet", "specific"} else "complet"
    start_age = int(interval.get("start_varsta", 0))
    end_age = int(interval.get("final_varsta", 108))
    if not (0 <= start_age < end_age <= 108):
        raise ValueError("Intervalul de vârstă trebuie să fie între 0 și 108.")

    person_id = f"{birth_date}-{ascii_slug(full_name)}"
    timestamp = now.astimezone().isoformat(timespec="seconds")
    return {
        "schema_version": 1,
        "id": person_id,
        "identitate": {
            "nume_complet": full_name,
            "nume_familie": require_text(identity.get("nume_familie"), "nume_familie"),
            "prenume": require_text(identity.get("prenume"), "prenume"),
            "prenume_activ": require_text(identity.get("prenume_activ"), "prenume_activ"),
            "data_nasterii": birth_date,
            "ora_nasterii": birth_time,
            "gen": gender,
            "nume_anterioare": [str(item).strip() for item in identity.get("nume_anterioare") or [] if str(item).strip()],
        },
        "preferinte_lucrare": {
            "template": preferences.get("template") or "examen",
            "exprimare": preferences.get("exprimare") if preferences.get("exprimare") in {"conversational", "formal"} else "conversational",
            "nivel_detaliere": preferences.get("nivel_detaliere") if preferences.get("nivel_detaliere") in {"scurt", "mediu", "amplu"} else "amplu",
            "interval_ani": {"tip": interval_type, "start_varsta": start_age, "final_varsta": end_age},
        },
        "intrebari": questions,
        "relatii": relations,
        "metadata": {"created_at": timestamp, "updated_at": timestamp},
    }


def filename_for(document: dict, now: datetime) -> str:
    identity = document["identitate"]
    stamp = now.astimezone().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{identity['data_nasterii']}-{ascii_slug(identity['nume_complet'])}__{stamp}.yaml"


def frontend_person(document: dict, source: Path) -> dict:
    identity = document.get("identitate") or {}
    preferences = document.get("preferinte_lucrare") or {}
    interval = preferences.get("interval_ani") or {}
    metadata = document.get("metadata") or {}
    return {
        "schemaVersion": document.get("schema_version", 1),
        "id": document.get("id") or f"{identity.get('data_nasterii', '')}-{ascii_slug(identity.get('nume_complet', ''))}",
        "recordKey": source.name,
        "fullName": identity.get("nume_complet", ""),
        "familyName": identity.get("nume_familie", ""),
        "givenNames": identity.get("prenume", ""),
        "activeName": identity.get("prenume_activ", ""),
        "birthDate": str(identity.get("data_nasterii", "")),
        "birthTime": identity.get("ora_nasterii"),
        "gender": identity.get("gen", ""),
        "previousNames": identity.get("nume_anterioare") or [],
        "questions": [{"category": item.get("categorie", "alta"), "text": item.get("text", "")} for item in document.get("intrebari") or []],
        "relations": [{
            "personId": item.get("persoana_id"),
            "fullName": item.get("nume", ""),
            "birthDate": str(item.get("data_nasterii", "")),
            "gender": item.get("gen", ""),
            "type": item.get("tip", "partener"),
            "status": item.get("status", "provizorie"),
        } for item in document.get("relatii") or []],
        "preferences": {
            "template": preferences.get("template", "examen"),
            "expression": preferences.get("exprimare", "conversational"),
            "detailLevel": preferences.get("nivel_detaliere", "amplu"),
            "ageRange": {
                "type": interval.get("tip", "complet"),
                "start": interval.get("start_varsta", 0),
                "end": interval.get("final_varsta", 108),
            },
        },
        "metadata": {
            "createdAt": str(metadata.get("created_at")) if metadata.get("created_at") is not None else None,
            "updatedAt": str(metadata.get("updated_at")) if metadata.get("updated_at") is not None else None,
        },
    }


def scan_persons() -> list[dict]:
    PERSONS_DIR.mkdir(parents=True, exist_ok=True)
    result = []
    for source in sorted(PERSONS_DIR.glob("*.yaml"), reverse=True):
        try:
            with source.open("r", encoding="utf-8") as handle:
                document = yaml.safe_load(handle) or {}
            result.append(frontend_person(document, source))
        except (OSError, yaml.YAMLError, ValueError, TypeError) as error:
            result.append({"recordKey": source.name, "error": str(error)})
    return result


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_json(self, payload: object, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if urlparse(self.path).path == "/api/persons":
            persons = scan_persons()
            errors = [item for item in persons if item.get("error")]
            self.send_json({"persons": [item for item in persons if not item.get("error")], "errors": errors})
            return
        super().do_GET()

    def do_POST(self) -> None:
        request_path = urlparse(self.path).path
        if request_path not in {"/api/persons", "/api/persons/import"}:
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_BODY_BYTES:
                raise ValueError("Dimensiunea datelor este invalidă.")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if request_path == "/api/persons/import":
                yaml_text = require_text(payload.get("yaml"), "fișier_yaml")
                try:
                    payload = yaml.safe_load(yaml_text) or {}
                except yaml.YAMLError as error:
                    raise ValueError(f"Fișierul YAML nu este valid: {error}") from error
                if not isinstance(payload, dict):
                    raise ValueError("Fișierul YAML trebuie să conțină fișa unei persoane.")
            now = datetime.now().astimezone()
            document = normalize_document(payload, now)
            PERSONS_DIR.mkdir(parents=True, exist_ok=True)
            target = PERSONS_DIR / filename_for(document, now)
            with target.open("x", encoding="utf-8", newline="\n") as handle:
                yaml.safe_dump(document, handle, allow_unicode=True, sort_keys=False, default_flow_style=False)
            self.send_json({
                "ok": True,
                "imported": request_path == "/api/persons/import",
                "file": target.name,
                "person": frontend_person(document, target),
            }, HTTPStatus.CREATED)
        except FileExistsError:
            self.send_json({"ok": False, "error": "Există deja o înregistrare creată în aceeași secundă."}, HTTPStatus.CONFLICT)
        except (ValueError, TypeError, json.JSONDecodeError) as error:
            self.send_json({"ok": False, "error": str(error)}, HTTPStatus.BAD_REQUEST)
        except OSError as error:
            self.send_json({"ok": False, "error": f"Fișierul nu a putut fi salvat: {error}"}, HTTPStatus.INTERNAL_SERVER_ERROR)


def main() -> None:
    parser = argparse.ArgumentParser(description="Server local Dashboard V3 cu registru YAML pentru persoane")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    print(f"Dashboard V3: http://{args.host}:{args.port}/#/dashboard")
    print(f"Registru persoane: {PERSONS_DIR}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
