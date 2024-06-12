# Makefile
.PHONY: test
test:
	poetry run pytest tests/

.PHONY: isort
isort:
	poetry run isort src

.PHONY: black
black:
	poetry run black --line-length 120 src

.PHONY: flake8
flake8:
	poetry run flake8 --ignore=E226,E302,E41,W191,W503 --max-complexity=13 --max-line-length=120 src

.PHONY: typing
typing:
	poetry run mypy src
	poetry run pyright src
