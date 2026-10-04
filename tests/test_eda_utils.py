import pandas as pd

from reposquad_ml_collab.eda_utils import summarize_missing_values


def test_summarize_missing_values():
    df = pd.DataFrame(
        {
            "name": ["A", "B", None],
            "age": [20, None, 22],
        }
    )

    result = summarize_missing_values(df)

    assert result.loc["name", "missing_count"] == 1
    assert result.loc["age", "missing_count"] == 1
    assert result.loc["name", "missing_percentage"] == 33.33