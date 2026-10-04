RepoSquad ML Collaboration Project

Git-based collaborative machine learning project using GitHub, DVC, reproducible experiments, CI, and reviewed pull requests.

Team

- Person 1: Fatima Tu Zahra - Model Owner + Platform/CI
- Person 2: Fatima Anjum - Data Owner + Platform/DVC

Dataset

Binary Classification with a Bank Dataset

The project uses the Bank Dataset from the Kaggle Playground Series S5E8 competition.

The dataset contains:

- train.csv - training data with the target variable y
- test.csv - test data for predictions
- sample_submission.csv - required submission format

Total dataset size: approximately 89.9 MB.

Source:
https://www.kaggle.com/competitions/playground-series-s5e8/data

The dataset is managed using DVC rather than being stored directly in Git.

Workflow

dev -> staging -> main

Main Tools

- Python
- uv
- pandas
- scikit-learn
- pytest
- Ruff
- Git
- GitHub
- DVC
- GitHub Actions