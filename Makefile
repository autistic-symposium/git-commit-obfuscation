.PHONY: vev install run

VENV = venv


venv:
	python3 -m $(VENV) $(VENV)
	source $(VENV)/bin/activate

install: venv
	pip3 install -r requirements.txt

run:
	python3 run.py

