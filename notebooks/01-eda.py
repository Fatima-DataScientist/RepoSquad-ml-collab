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
# ---

# %% [markdown]
# # 01 - EDA

# %%
import sys
sys.path.append("..")
import pandas as pd
from src.clean import drop_duplicates_and_nulls

# %%
df = pd.read_csv("../data/raw/YOUR_FILE.csv")
df.head()

# %%
df.info()

# %%
df.isna().sum()

# %%
df_clean = drop_duplicates_and_nulls(df)
print(df.shape, "->", df_clean.shape)
