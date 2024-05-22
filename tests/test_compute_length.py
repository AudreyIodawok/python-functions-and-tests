import pytest
from typing import Optional
from source.fonctions import compute_length

# --------------------------------------------------------------------------------------------------
# fonction compute_length (fonction n°10)
# --------------------------------------------------------------------------------------------------

#def compute_length(word: Optional[str]) -> int:
    #return len(word) if word else 0


@pytest.mark.parametrize("word, length", [
    ("", 0),
    ("bert", 4),
    (None, 0)
])
def test_compute_length(word: str, length: int):
    assert compute_length(word) == length