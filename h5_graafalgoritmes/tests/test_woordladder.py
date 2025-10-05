# tests/test_woordladder.py
import pytest
from pathlib import Path

# PAS HIER AAN naar jouw modulepad
from h5_graafalgoritmes.woordladder import (
    precies_een_verschillend,
    maak_graaf,
    kortste_pad,
    geef_pad,
)

# ---------- Case 0: precies_een_verschillend ----------
@pytest.mark.timeout(1)
def test_precies_een_verschillend_examples():
    assert precies_een_verschillend("span", "spat") is True
    assert precies_een_verschillend("test", "tast") is True
    assert precies_een_verschillend("test", "test") is False
    assert precies_een_verschillend("test", "testje") is False
    assert precies_een_verschillend("testje", "test") is False
    assert precies_een_verschillend("TEST", "test") is False


# ---------- Case 1: maak_graaf ----------
@pytest.mark.timeout(1)
def test_maak_graaf_2letters():
    words = ["aa", "ab", "ac", "ad",
             "ba", "bb", "bc", "bd",
             "ca", "cb", "cc", "cd",
             "da", "db", "dc", "dd"]
    g = maak_graaf(words)
    expected = {
        'aa': {'ac', 'ca', 'ab', 'ba', 'da', 'ad'},
        'ab': {'aa', 'ac', 'cb', 'db', 'bb', 'ad'},
        'ac': {'aa', 'dc', 'ab', 'bc', 'cc', 'ad'},
        'ad': {'ac', 'ab', 'dd', 'cd', 'bd', 'aa'},
        'ba': {'ca', 'bc', 'bd', 'da', 'bb', 'aa'},
        'bb': {'ab', 'bc', 'ba', 'bd', 'cb', 'db'},
        'bc': {'ac', 'dc', 'ba', 'bd', 'bb', 'cc'},
        'bd': {'dd', 'bc', 'cd', 'ba', 'bb', 'ad'},
        'ca': {'cd', 'ba', 'da', 'cb', 'cc', 'aa'},
        'cb': {'ca', 'ab', 'cd', 'db', 'bb', 'cc'},
        'cc': {'ac', 'ca', 'dc', 'bc', 'cd', 'cb'},
        'cd': {'ca', 'dd', 'bd', 'cb', 'cc', 'ad'},
        'da': {'ca', 'dc', 'dd', 'ba', 'db', 'aa'},
        'db': {'dc', 'ab', 'cb', 'dd', 'da', 'bb'},
        'dc': {'ac', 'dd', 'bc', 'da', 'db', 'cc'},
        'dd': {'dc', 'cd', 'bd', 'da', 'db', 'ad'},
    }
    assert g == expected


# ---------- Case 2: kortste_pad ----------
@pytest.mark.timeout(1)
def test_kortste_pad_from_aa_pred_map():
    words = ["aa", "ab", "ac", "ad",
             "ba", "bb", "bc", "bd",
             "ca", "cb", "cc", "cd",
             "da", "db", "dc", "dd"]
    g = maak_graaf(words)
    pred = kortste_pad(g, "aa")
    expected_pred = {
        'aa': 'aa', 'ab': 'aa', 'ac': 'aa', 'ad': 'aa',
        'ba': 'aa', 'bb': 'ab', 'bc': 'ac', 'bd': 'ad',
        'ca': 'aa', 'cb': 'ab', 'cc': 'ac', 'cd': 'ad',
        'da': 'aa', 'db': 'ab', 'dc': 'ac', 'dd': 'ad'
    }
    assert pred == expected_pred


# ---------- Case 3: geef_pad ----------
@pytest.mark.timeout(1)
def test_geef_pad_examples():
    words = ["aa", "ab", "ac", "ad",
             "ba", "bb", "bc", "bd",
             "ca", "cb", "cc", "cd",
             "da", "db", "dc", "dd"]
    g = maak_graaf(words)
    pred = kortste_pad(g, "aa")
    assert geef_pad(pred, "dd") == ['aa', 'ad', 'dd']
    assert geef_pad(pred, "aa") == ['aa']
    assert geef_pad(pred, "ba") == ['aa', 'ba']


# h5_graafalgoritmes/tests/test_woordladder_case4.py
import pytest
from pathlib import Path

# PAS AAN naar jouw modulepad:
from h5_graafalgoritmes.woordladder import maak_graaf, kortste_pad, geef_pad


# h5_graafalgoritmes/tests/test_woordladder_case4_transcribed.py
import pytest
from pathlib import Path

# PAS AAN naar jouw modulepad:
from h5_graafalgoritmes.woordladder import maak_graaf, kortste_pad, geef_pad

@pytest.mark.timeout(50)  # maak_graaf is O(n^2) op 5757 woorden: geef wat tijd
def test_case4_transcribed_from_repl():
    here = Path(__file__).parent
    words_path = here / "sgb-words.txt"

    # 1) woordenlijst laden (zoals in 4.in)
    words = [w.strip() for w in words_path.read_text(encoding="utf-8").splitlines()]
    assert len(words) == 5757  # sanity check uit je REPL

    # 2) graaf bouwen
    graaf = maak_graaf(words)

    # 3) lokale buur-sets (exact zoals in 4.in)
    assert graaf['which'] == {'whish'}
    assert graaf['whish'] == {'whisk', 'shish', 'which', 'whist'}
    assert graaf['shish'] == {'whish', 'shush', 'swish'}
    assert graaf['shush'] == {'shish', 'slush'}
    assert graaf['slush'] == {'shush', 'plush', 'slash', 'slosh', 'flush', 'blush'}
    assert graaf['blush'] == {'brush', 'plush', 'slush', 'flush', 'blash'}

    # 4) kortste paden vanaf 'which'
    pred = kortste_pad(graaf, 'which')
    assert pred['blush'] == 'slush'
    assert pred['slush'] == 'shush'

    # expliciet pad naar 'blush'
    assert geef_pad(pred, 'blush') == ['which', 'whish', 'shish', 'shush', 'slush', 'blush']

    # aantal woorden verbonden met 'which'
    connected_count = sum(1 for w in words if pred[w] is not None)
    assert connected_count == 4493

    # alfabetisch kleinste en grootste woord NIET verbonden met 'which'
    not_connected_sorted = sorted([w for w in words if pred[w] is None])
    assert not_connected_sorted[0] == 'aargh'
    assert not_connected_sorted[-1] == 'zowie'

    # buurinfo voor 'aargh' en 'zowie'
    assert graaf['aargh'] == set()
    assert graaf['zowie'] == {'bowie'}

    # 5) woorden met pad naar 'zowie'
    pred2 = kortste_pad(graaf, 'zowie')
    reachable_zowie = sorted([w for w in words if pred2[w] is not None])
    assert reachable_zowie == ['bogie', 'bowie', 'dogie', 'doxie', 'movie', 'moxie', 'zowie']
