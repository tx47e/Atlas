import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml


MODULE_PATH = Path(__file__).with_name("gestioneaza_persoane.py")
SPEC = importlib.util.spec_from_file_location("gestioneaza_persoane", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


def profile(name="Șerban Ana-Maria", birth="2000-02-29"):
    return {
        "identitate": {
            "nume_complet": name,
            "nume_familie": "Șerban",
            "prenume": "Ana-Maria",
            "prenume_activ": "Ana",
            "data_nasterii": birth,
            "gen": "feminin",
            "nume_anterioare": [],
        },
        "preferinte_lucrare": {
            "template": "examen",
            "exprimare": "conversational",
            "nivel_detaliere": "amplu",
            "interval_ani": {"tip": "complet", "start_varsta": 0, "final_varsta": 108},
        },
        "intrebari": [{"categorie": "cariera", "text": "Care este direcția potrivită?"}],
        "relatii": [
            {
                "persoana_id": None,
                "nume": "Pop Ion",
                "data_nasterii": None,
                "tip": "partener",
                "status": "provizorie",
            }
        ],
    }


class RegistryTests(unittest.TestCase):
    def test_identifier_transliterates_diacritics(self):
        self.assertEqual(
            MODULE.person_id("29.02.2000", "Șerban Ana-Maria"),
            "2000-02-29-SERBAN-ANA-MARIA",
        )

    def test_normalize_complete_profile(self):
        with tempfile.TemporaryDirectory() as temp:
            result = MODULE.normalize_profile(profile(), Path(temp))
        self.assertEqual(result["schema_version"], 1)
        self.assertIsNone(result["identitate"]["ora_nasterii"])
        self.assertEqual(result["preferinte_lucrare"]["interval_ani"]["final_varsta"], 108)
        self.assertEqual(result["relatii"][0]["status"], "provizorie")

    def test_birth_time_is_optional_and_normalized(self):
        value = profile()
        value["identitate"]["ora_nasterii"] = "07:05"
        with tempfile.TemporaryDirectory() as temp:
            result = MODULE.normalize_profile(value, Path(temp))
        self.assertEqual(result["identitate"]["ora_nasterii"], "07:05")

    def test_invalid_birth_time_is_rejected(self):
        for invalid in ("7:05", "24:00", "12:60", "dimineața"):
            value = profile()
            value["identitate"]["ora_nasterii"] = invalid
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as temp:
                with self.assertRaises(MODULE.ValidationError):
                    MODULE.normalize_profile(value, Path(temp))

    def test_future_birth_date_is_rejected(self):
        future = f"{date.today().year + 1}-01-01"
        with tempfile.TemporaryDirectory() as temp, self.assertRaises(MODULE.ValidationError):
            MODULE.normalize_profile(profile(birth=future), Path(temp))

    def test_exact_collision_requires_update(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "persoane"
            source = Path(temp) / "draft.yaml"
            source.write_text(yaml.safe_dump(profile(), allow_unicode=True), encoding="utf-8")
            args = type("Args", (), {"confirmat": True, "root": root, "input": source, "actualizare": False})
            self.assertEqual(MODULE.command_save(args), 0)
            with self.assertRaises(MODULE.ValidationError):
                MODULE.command_save(args)

    def test_save_requires_confirmation(self):
        with tempfile.TemporaryDirectory() as temp:
            args = type(
                "Args",
                (),
                {"confirmat": False, "root": Path(temp), "input": Path(temp) / "missing", "actualizare": False},
            )
            with self.assertRaises(MODULE.ValidationError):
                MODULE.command_save(args)

    def test_unknown_schema_version_is_rejected(self):
        value = profile()
        value["schema_version"] = 2
        with tempfile.TemporaryDirectory() as temp, self.assertRaises(MODULE.ValidationError):
            MODULE.normalize_profile(value, Path(temp))

    def test_confirmed_relation_requires_existing_person(self):
        value = profile()
        value["relatii"][0]["status"] = "confirmata"
        value["relatii"][0]["persoana_id"] = "1990-01-01-POP-ION"
        with tempfile.TemporaryDirectory() as temp, self.assertRaises(MODULE.ValidationError):
            MODULE.normalize_profile(value, Path(temp))


if __name__ == "__main__":
    unittest.main()
