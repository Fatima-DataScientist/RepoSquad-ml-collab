# Contributing Guide

## Permanent Branches

- `main` — production/released model
- `staging` — release candidate
- `dev` — integration branch

## Short-Lived Branches

- `feat/<name>` — features and pipeline changes
- `data/<name>` — dataset changes tracked with DVC
- `exp/<member>-<idea>` — experiments
- `fix/<name>` — urgent production fixes

## Commit Convention

We use Conventional Commits.

Examples:

- `feat: add training pipeline`
- `data: track initial dataset`
- `fix: correct preprocessing`
- `exp: try max_depth=10`
- `docs: update README`
- `test: add unit tests`

## Pull Requests

After initial setup:

- No direct pushes to `main`
- No direct pushes to `staging`
- No direct pushes to `dev`
- All changes must arrive through pull requests
- Every PR must be reviewed by the other team member

## Merge Strategy

We will use squash merging for pull requests into `dev`.