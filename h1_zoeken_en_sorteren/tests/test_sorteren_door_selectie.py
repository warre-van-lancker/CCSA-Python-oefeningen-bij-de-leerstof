# h1_zoeken_en_sorteren/tests/test_sorteren_door_selectie.py
import sys
import subprocess
import pytest

# PAS HIER AAN naar jouw modulepad (zonder .py):
MODULE = "h1_zoeken_en_sorteren.sorteren_door_selectie"

def _run(stdin_text: str) -> list[str]:
    """Voer het modulebestand uit als script en geef stdout-regels terug."""
    proc = subprocess.run(
        [sys.executable, "-m", MODULE],
        input=stdin_text.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return proc.stdout.decode().splitlines()

def _expected_selection_lines_from_input(stdin_text: str) -> list[str]:
    """Bereken de verwachte tussenprints zoals jouw selection_sort_vooraan ze maakt."""
    data = stdin_text.strip()
    a = [int(x) for x in data.split()] if data else []
    out = []
    n = len(a)
    for i in range(n - 1):
        positie = i
        m = a[i]
        for j in range(i + 1, n, 1):
            if a[j] < m:
                positie = j
                m = a[j]
        a[positie] = a[i]
        a[i] = m
        out.append(str(a))
    return out

@pytest.mark.timeout(1)
@pytest.mark.parametrize("stdin_text", [
    "\n",                # leeg
    "42\n",              # één element
    "1 2 3\n",           # al gesorteerd
    "3 2 1\n",           # omgekeerd
    "2 1 2 1\n",         # dubbels
    "44 55 12 42 94 18 6 67\n",  # jouw extra case
])
def test_selection_sort_vooraan(stdin_text):
    actual_lines = _run(stdin_text)
    expected_lines = _expected_selection_lines_from_input(stdin_text)
    assert actual_lines == expected_lines
