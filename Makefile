.PHONY: all tests clean

install-dev:
	pip install pre-commit
	pre-commit install
	pre-commit install --hook-type pre-push
	make build-dev

build-dev:
	pip install --no-cache-dir -U pip poetry
	poetry install

tests:
	poetry run python -m pytest -v tests

format:
	poetry run isort .
	poetry run black .

check:
	poetry run isort . -c
	poetry run black . --check

run:
	poetry run python simulate.py
