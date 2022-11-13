VENV = venv
PYTHON = (VENV)/bin/python3
PIP = (VENV)/bin/pip

run: $(VENV)/bin/activate
	(PYTHON) main.py


(VENV)/bin/activate: setup.py
	python3 -m venv (VENV)
	(PIP) install -r setup.py


clean:
	rm -rf __pycache__
	rm -rf (VENV)