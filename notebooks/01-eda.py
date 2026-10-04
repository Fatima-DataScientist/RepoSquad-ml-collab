# ---
# jupyter:
#   jupytext:

#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
###Exploratory Data Analysis

# This notebook performs an initial exploratory data analysis of the bank marketing dataset.

# The analysis includes:
# - Dataset dimensions and structure
# - Missing-value analysis
# - Data types
# - Summary statistics
# - Target variable distribution
# - Numerical feature distributions
# - Categorical feature distributions

# %%
import matplotlib.pyplot as plt
import pandas as pd

from reposquad_ml_collab.features import clean_column_names

pd.set_option("display.max_columns", None)

# %%
DATA_PATH = "data/raw/playground-series-s5e8/train.csv"

df = pd.read_csv(DATA_PATH)

df = clean_column_names(df)

print(f"Dataset shape: {df.shape}")
df.head()

# %%
## Dataset Structure

# The dataset contains 750,000 observations and 18 columns. The target variable is `y`.

# %%
df.info()

# %%
df.isnull().sum().sort_values(ascending=False)

# %%
df.describe(include="all").T

# %%
## Target Variable

# The target variable `y` indicates whether the customer subscribed to the term deposit.

# %%
target_counts = df["y"].value_counts()

print(target_counts)
print("\nTarget proportions:")
print(df["y"].value_counts(normalize=True))

# %%
target_counts.plot(kind="bar")

plt.title("Target Variable Distribution")
plt.xlabel("Target")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()

# %%
## Numerical Features

# We inspect the distributions of important numerical variables such as age, balance, duration, campaign, pdays, and previous contacts.

# %%
numerical_columns = [
    "age",
    "balance",
    "day",
    "duration",
    "campaign",
    "pdays",
    "previous",
]

df[numerical_columns].describe().T

# %%
df[numerical_columns].hist(
    figsize=(12, 10),
    bins=30,
)

plt.suptitle("Numerical Feature Distributions")
plt.tight_layout()
plt.show()

# %%
## Categorical Features

# We examine the most important categorical variables and their value frequencies.

# %%
categorical_columns = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "poutcome",
]

for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].value_counts(dropna=False).head(10))

# %%
## EDA Summary

# The dataset contains 750,000 rows and 18 columns.

# The analysis shows:
# - The dataset structure and data types.
# - Missing-value counts for each feature.
# - Summary statistics for numerical and categorical variables.
# - The distribution of the target variable `y`.
# - Distributions of numerical features.
# - Frequency distributions of categorical features.

# The reusable `clean_column_names` function from the project source code was imported and used to standardize the column names.

# %%

# %%

# %%

# %%

# %%

# %%

# %%
