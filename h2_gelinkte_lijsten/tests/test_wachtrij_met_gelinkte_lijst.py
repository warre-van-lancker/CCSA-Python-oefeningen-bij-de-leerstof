# h1_zoeken_en_sorteren/tests/test_queue_list.py
import pytest

# PAS DIT PAD AAN indien nodig:
from h2_gelinkte_lijsten.wachtrij_met_gelinkte_lijst import QueueList


@pytest.mark.timeout(5)
def test_queuelist_dodona_case_0():
    # === komt overeen met 0.in / 0.out ===
    q = QueueList()
    assert q.empty() is True

    q.enqueue("One")
    assert q.empty() is False
    assert q.front() == "One"

    q.enqueue("Two")
    q.enqueue("Three")
    assert q.front() == "One"

    assert q.dequeue() == "One"
    assert q.dequeue() == "Two"
    assert q.front() == "Three"
    assert q.empty() is False

    q.enqueue("Four")
    assert q.dequeue() == "Three"
    assert q.dequeue() == "Four"
    assert q.empty() is True


@pytest.mark.timeout(5)
def test_queuelist_dodona_case_1_invert():
    # === komt overeen met 1.in / 1.out ===
    q = QueueList()
    for x in range(1, 5):
        q.enqueue(x)

    assert q.front() == 1

    q.invert()
    assert q.front() == 4
    assert q.dequeue() == 4
    assert q.front() == 3

    q.invert()
    assert q.front() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.front() == 3

    q.invert()
    assert q.front() == 3
    assert q.dequeue() == 3

    q.invert()
    assert q.empty() is True

    q.enqueue(10)
    assert q.front() == 10
