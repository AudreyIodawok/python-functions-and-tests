import pytest
import pandas as pd
from typing import Collection
from source.fonctions import find_max_element

# --------------------------------------------------------------------------------------------------
# fonction find_max_element(fonction n°8 bis)
# --------------------------------------------------------------------------------------------------

# def find_max_element(collection: Collection) -> int:
#     return max(collection) if len(collection) else 0

@pytest.mark.parametrize("collection, result", [
    ([], 0),
    ([4], 4),
    ([4, 7], 7),
    (pd.Series([4, 7]), 7),
])
def test_find_max_element(collection: Collection, result: int):
    assert find_max_element(collection) == result