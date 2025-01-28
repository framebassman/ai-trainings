venv:
	python3.10 -m venv .venv

poetry-venv:
	poetry env use $$(which python3.10)
