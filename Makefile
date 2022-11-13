target: lib

clear:
	python -m clear __pycache__, venv, dist, LibraryPractice,egg-info

run: 
	python -m build
