from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "generate_omulet_relatiilor.py"
)
SPEC = importlib.util.spec_from_file_location("generate_omulet_relatiilor", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class BirthDateDigitsTests(unittest.TestCase):
    def test_formatting_zeroes_are_removed(self) -> None:
        self.assertEqual(
            MODULE.birth_date_digits("01.09.1990"),
            [1, 9, 1, 9, 9, 0],
        )

    def test_real_zeroes_are_preserved(self) -> None:
        self.assertEqual(
            MODULE.birth_date_digits("10.10.1990"),
            [1, 0, 1, 0, 1, 9, 9, 0],
        )
        self.assertEqual(
            MODULE.birth_date_digits("20.09.2001"),
            [2, 0, 9, 2, 0, 0, 1],
        )

    def test_supported_separators_are_equivalent(self) -> None:
        expected = [1, 2, 1, 1, 9, 9, 8]
        for value in ("12.01.1998", "12/01/1998", "12-01-1998"):
            with self.subTest(value=value):
                self.assertEqual(MODULE.birth_date_digits(value), expected)


if __name__ == "__main__":
    unittest.main()
