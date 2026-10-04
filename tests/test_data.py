import pandas as pd

from reposquad_ml_collab.features import clean_column_names


def test_clean_column_names():
    df = pd.DataFrame(
        {
            " First Name ": ["Fatima"],
            "Age ": [20],
            "Education Level": ["Bachelor"],
        }
    )

    cleaned_df = clean_column_names(df)

    assert list(cleaned_df.columns) == [
        "first_name",
        "age",
        "education_level",
    ]
