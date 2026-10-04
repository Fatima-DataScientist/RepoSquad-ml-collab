import os
import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open("params.yaml"))
df = pd.read_csv(params["data"]["path"])
if "id" in df.columns:
    df = df.drop(columns=["id"])

train, test = train_test_split(
    df,
    test_size=params["split"]["test_size"],
    random_state=params["seed"],
    stratify=df[params["data"]["target"]],
)
os.makedirs("data/processed", exist_ok=True)
train.to_csv("data/processed/train.csv", index=False)
test.to_csv("data/processed/test.csv", index=False)