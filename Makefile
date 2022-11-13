target: setup.py

run: 
	python -m build

test:
	python -m test

clear:
	python -m clear __pycache__, venv
