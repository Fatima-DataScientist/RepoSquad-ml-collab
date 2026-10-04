import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataframe column names by stripping spaces and converting to lowercase."""
    cleaned_df = df.copy()
    cleaned_df.columns = cleaned_df.columns.str.strip().str.lower().str.replace(" ", "_")
    return cleaned_df
