import pytest
import pandas as pd

# --------------------------------------------------------------------------------------------------
# Test fonction create_name_len_col (fonction n°8)
# --------------------------------------------------------------------------------------------------

from source.fonctions import create_name_len_col 

@pytest.mark.parametrize("series1, series2", [
    (pd.Series([]), pd.Series([])),
    (pd.Series(["bert"]), pd.Series([4])),
    (pd.Series(["bert", "roberta"]), pd.Series([4, 7]))
])
def test_create_name_len_col(series1: pd.Series, series2: pd.Series):
    pd.testing.assert_series_equal(create_name_len_col(series1), series2, check_dtype=False)
