import pandas as pd

def drop_duplicates_and_nulls(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().dropna().reset_index(drop=True)