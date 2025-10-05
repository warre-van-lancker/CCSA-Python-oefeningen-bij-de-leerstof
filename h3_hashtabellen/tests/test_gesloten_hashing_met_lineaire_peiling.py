import pytest

# PAS DIT PAD AAN indien nodig:
from h3_hashtabellen.gesloten_hashing_met_lineaire_peiling import HashSet


@pytest.mark.timeout(2)
def test_empty_then_add_and_index_basic():
    h = HashSet(max_size=10)
    # leeg
    assert h.index_of(123) == -1

    # toevoegen en terugvinden
    i10 = h.add(10)
    i15 = h.add(15)
    i29 = h.add(29)

    assert 0 <= i10 < 10
    assert 0 <= i15 < 10
    assert 0 <= i29 < 10

    assert h.index_of(10) == i10
    assert h.index_of(15) == i15
    assert h.index_of(29) == i29

    # iets dat er niet in staat
    assert h.index_of(999) == -1


@pytest.mark.timeout(2)
def test_linear_probing_collisions_same_bucket():
    # Met integers is hash(x) == x, dus modulo is voorspelbaar
    h = HashSet(max_size=7)
    # 0, 7, 14 botsen allemaal op index 0
    i0 = h.add(0)    # -> index 0
    i7 = h.add(7)    # -> index 1
    i14 = h.add(14)  # -> index 2

    assert (i0, i7, i14) == (0, 1, 2)
    assert h.index_of(0) == 0
    assert h.index_of(7) == 1
    assert h.index_of(14) == 2


@pytest.mark.timeout(2)
def test_wraparound_and_tombstone_reuse():
    # Forceer wrap-around en test dat deleted slot wordt hergebruikt
    h = HashSet(max_size=5)

    # Vul aaneengesloten indices op 0..3
    # 0%5=0, 5%5=0 -> 1, 10%5=0 -> 2, 15%5=0 -> 3
    a = h.add(0)    # 0
    b = h.add(5)    # 1
    c = h.add(10)   # 2
    d = h.add(15)   # 3
    assert (a, b, c, d) == (0, 1, 2, 3)

    # delete element op index 1 (waarde 5) -> tombstone
    assert h.delete(5) is True
    assert h.index_of(5) == -1

    # wrap-around check: toevoegen van 20 (hash 0) loopt tegen 0, gaat naar 1 (tombstone reused)
    e = h.add(20)
    assert e == 1
    assert h.index_of(20) == 1

    # bestaande elementen blijven vindbaar, ondanks tombstone in de keten
    assert h.index_of(0) == 0
    assert h.index_of(10) == 2
    assert h.index_of(15) == 3


@pytest.mark.timeout(2)
def test_delete_then_search_chain_through_deleted():
    h = HashSet(max_size=5)
    # 0, 5, 10 -> indices 0,1,2
    h.add(0)
    h.add(5)
    h.add(10)
    # verwijder 5 (index 1), maar 10 moet nog vindbaar zijn (door deleted heen)
    assert h.delete(5) is True
    assert h.index_of(10) == 2
    # opnieuw 5 is niet aanwezig
    assert h.index_of(5) == -1


@pytest.mark.timeout(2)
def test_table_full_raises_valueerror():
    h = HashSet(max_size=3)
    h.add(1)
    h.add(2)
    h.add(3)
    with pytest.raises(ValueError):
        h.add(4)  # set is vol


@pytest.mark.timeout(2)
def test_delete_nonexistent_returns_false():
    h = HashSet(max_size=4)
    h.add(1)
    assert h.delete(999) is False
    # bestaand element blijft vindbaar
    assert h.index_of(1) != -1
