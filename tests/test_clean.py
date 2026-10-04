import pandas as pd
from src.clean import drop_duplicates_and_nulls

def test_drop_duplicates_and_nulls():
    df = pd.DataFrame({"a": [1, 1, 2, None], "b": [3, 3, 4, 5]})
    out = drop_duplicates_and_nulls(df)
    assert len(out) == 2