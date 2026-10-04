import json
import subprocess
import joblib
import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

params = yaml.safe_load(open("params.yaml"))
target = params["data"]["target"]

test = pd.read_csv("data/processed/test.csv")
X, y = test.drop(columns=[target]), test[target]
model = joblib.load("models/model.pkl")

proba = model.predict_proba(X)[:, 1]
pred = model.predict(X)

try:
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
except Exception:
    sha = "unknown"

metrics = {
    "roc_auc": round(roc_auc_score(y, proba), 6),
    "accuracy": round(accuracy_score(y, pred), 6),
    "f1": round(f1_score(y, pred), 6),
    "commit": sha,
}
json.dump(metrics, open("metrics.json", "w"), indent=2)
print(metrics)