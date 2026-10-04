import pandas as pd


def summarize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing-value counts and percentages for each column."""
    missing = df.isna().sum()
    percentage = (missing / len(df) * 100).round(2)

    return pd.DataFrame(
        {
            "missing_count": missing,
            "missing_percentage": percentage,
        }
    ).sort_values("missing_count", ascending=False)