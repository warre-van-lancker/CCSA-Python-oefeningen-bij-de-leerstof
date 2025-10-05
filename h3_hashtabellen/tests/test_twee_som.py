# hX_yourfolder/tests/test_two_sum.py
import pytest

# PAS HIER AAN naar jouw modulepad:
from h3_hashtabellen.twee_som import two_sum, two_sum_hash

# Dodona 0.in / 0.out – exact dezelfde scenario's en verwachtte resultaten
CASES = [
    # doel = 10
    ([1, 4, 5, 7, 8, 9], 10, (0, 5)),
    # doel = 20
    ([1, 5, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 19], 20, (0, 12)),
    # doel = 50 (met 49 als laatste in korte lijst)
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
      21, 22, 23, 24, 25, 49], 50, (0, 25)),
    # doel = 50 (zelfde set maar met extra '1' op het einde → eerste geldige paar op indices 24 en 25)
    ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
      22, 23, 24, 25, 49, 1], 50, (24, 25)),
    # geen oplossing
    ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
      22, 23, 24, 25, 49], 50, None),
]

@pytest.mark.timeout(2)
@pytest.mark.parametrize("nums, target, expected", CASES,
                         ids=["10-ok","20-ok","50-front","50-tail","50-none"])
def test_twoSum(nums, target, expected):
    assert two_sum(nums, target) == expected

@pytest.mark.timeout(2)
@pytest.mark.parametrize("nums, target, expected", CASES,
                         ids=["10-ok","20-ok","50-front","50-tail","50-none"])
def test_twoSumHash(nums, target, expected):
    assert two_sum_hash(nums, target) == expected
