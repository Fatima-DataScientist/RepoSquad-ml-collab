import json
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import yaml

ROOT = Path(__file__).resolve().parents[3]

DATA_PATH = ROOT / "data/raw/playground-series-s5e8/train.csv"
PARAMS_PATH = ROOT / "configs/params.yaml"
METRICS_PATH = ROOT / "reports/metrics.json"
MODEL_PATH = ROOT / "models/model.joblib"


def load_params():
    with open(PARAMS_PATH, encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
    params = load_params()

    df = pd.read_csv(DATA_PATH)

    target = "y"

    # Use numeric columns for this simple reproducible baseline.
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    numeric_columns.remove(target)

    X = df[numeric_columns].fillna(0)
    y = df[target]

    test_size = params["data"]["test_size"]
    random_state = params["data"]["random_state"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=params["model"]["n_estimators"],
        max_depth=params["model"]["max_depth"],
        random_state=params["model"]["random_state"],
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(METRICS_PATH, "w", encoding="utf-8") as file:
        json.dump({"accuracy": accuracy}, file, indent=2)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    import joblib

    joblib.dump(model, MODEL_PATH)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Metrics saved to {METRICS_PATH}")
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
