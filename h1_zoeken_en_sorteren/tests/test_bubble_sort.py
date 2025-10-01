# h1_zoeken_en_sorteren/tests/test_bubble_sort.py
import sys
import subprocess
import pytest

MODULE = "h1_zoeken_en_sorteren.bubble_sort"

def _run(stdin_text: str) -> list[str]:
    proc = subprocess.run(
        [sys.executable, "-m", MODULE],
        input=stdin_text.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return proc.stdout.decode().splitlines()


@pytest.mark.parametrize("stdin_text, expected_lines", [
    ("\n", [
        "Voor een rij van lengte 0 werd het if-statement 0 keer uitgevoerd"
    ]),
    ("42\n", [
        "Voor een rij van lengte 1 werd het if-statement 0 keer uitgevoerd"
    ]),
    ("1 2 3\n", [
        "[1, 2, 3]",
        "[1, 2, 3]",
        "Voor een rij van lengte 3 werd het if-statement 3 keer uitgevoerd"
    ]),
    ("3 2 1\n", [
        "[1, 3, 2]",
        "[1, 2, 3]",
        "Voor een rij van lengte 3 werd het if-statement 3 keer uitgevoerd"
    ]),
    ("2 1 2 1\n", [
        "[1, 2, 1, 2]",
        "[1, 1, 2, 2]",
        "[1, 1, 2, 2]",
        "Voor een rij van lengte 4 werd het if-statement 6 keer uitgevoerd"
    ]),
    ("44 55 12 42 94 18 6 67\n", [
        "[6, 44, 55, 12, 42, 94, 18, 67]",
        "[6, 12, 44, 55, 18, 42, 94, 67]",
        "[6, 12, 18, 44, 55, 42, 67, 94]",
        "[6, 12, 18, 42, 44, 55, 67, 94]",
        "[6, 12, 18, 42, 44, 55, 67, 94]",
        "[6, 12, 18, 42, 44, 55, 67, 94]",
        "[6, 12, 18, 42, 44, 55, 67, 94]",
        "Voor een rij van lengte 8 werd het if-statement 28 keer uitgevoerd"
    ]),
])


def test_bubble_sort_cases(stdin_text, expected_lines):
    lines = _run(stdin_text)
    assert lines == expected_lines

