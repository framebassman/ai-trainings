venv:
	python3.9 -m venv .venv

poetry-venv:
	poetry env use $$(which python3)
