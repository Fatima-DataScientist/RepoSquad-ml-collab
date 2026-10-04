import os
import joblib
import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

params = yaml.safe_load(open("params.yaml"))
target = params["data"]["target"]
seed = params["seed"]
t = params["train"]

train = pd.read_csv("data/processed/train.csv")
X, y = train.drop(columns=[target]), train[target]
cat_cols = X.select_dtypes(include="object").columns.tolist()

# preprocessing is fit inside the pipeline, on the training split only
pre = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)],
    remainder="passthrough",
)
model = Pipeline([
    ("pre", pre),
    ("rf", RandomForestClassifier(
        n_estimators=t["n_estimators"],
        max_depth=t["max_depth"],
        random_state=seed,
        n_jobs=-1,
    )),
])
model.fit(X, y)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")