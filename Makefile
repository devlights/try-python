default: run

prepare:
	python3 -m pip install -U -r requirements_dev.txt
	python3 -m pip install -U -r requirements.txt

run:
	python -m trypython
