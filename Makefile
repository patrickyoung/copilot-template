.PHONY: install run clean test

VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python
REQUIREMENTS=requirements-dev.txt

install: ${VENV_NAME}/bin/activate

${VENV_NAME}/bin/activate: ${REQUIREMENTS}
	@test -d ${VENV_NAME} || python3 -m venv ${VENV_NAME}
	@. ${VENV_NAME}/bin/activate; pip install -U pip; pip install -r ${REQUIREMENTS}
	@touch ${VENV_NAME}/bin/activate

run: install
	@echo "Starting the application..."
	@${PYTHON} app.py

clean:
	@echo "Cleaning up..."
	@rm -rf ${VENV_NAME}
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

test: install
	@echo "Running tests..."
	@${PYTHON} -m pytest

test_long: install
	@echo "Running long tests..."
	@${VENV_NAME}/bin/pyresttest http://localhost:5000 tests/functional/*.yaml

help:
	@echo "Makefile commands:"
	@echo "install  : Setup the Python virtual environment and install dependencies."
	@echo "run      : Run the application."
	@echo "clean    : Remove virtual environment and pycache files."
	@echo "test     : Run the application tests."
	@echo "test     : Run the functiaonal / acceptance tests."
