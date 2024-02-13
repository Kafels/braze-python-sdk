#! /usr/bin/env make
VENV_BIN ?= python3 -m venv
PYTHON_CMD ?= python3
PIP_CMD ?= pip3

VENV_DIR ?= venv

VENV_ACTIVATE = $(VENV_DIR)/bin/activate

VENV_RUN = . $(VENV_ACTIVATE)

# Application path
APP_ROOT_PATH := ./code/braze
UNIT_TESTS_PATH := ./code/tests/unit


usage:    ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/:.*##\s*/##/g' | awk -F'##' '{ printf "%-40s %s\n", $$1, $$2 }'


$(VENV_ACTIVATE): setup.py
	test -d $(VENV_DIR) || $(VENV_BIN) $(VENV_DIR)
	$(VENV_RUN); $(PIP_CMD) install --upgrade pip setuptools wheel plux
	touch $(VENV_ACTIVATE)


venv: $(VENV_ACTIVATE)    ## Create a new (empty) dev virtual environment


# Install ONLY dev libraries
install: venv    ## Install all dependencies for dev environment
	$(VENV_RUN); $(PIP_CMD) install -r requirements.txt
	$(VENV_RUN); $(PIP_CMD) install -r requirements-build.txt
	$(VENV_RUN); $(PIP_CMD) install -r requirements-test.txt


test-unit: venv    ## Run the unit tests
	$(VENV_RUN); export PYTHONPATH=${APP_ROOT_PATH} \
	&& pytest --cov-report term-missing --cov-config=.coveragerc --cov=${APP_ROOT_PATH} ${UNIT_TESTS_PATH} -s -vv


build: venv clean-dist
	$(VENV_RUN); $(PYTHON_CMD) -m build
	$(VENV_RUN); twine check dist/*


publish: venv
	$(VENV_RUN); twine upload dist/*

clean:    ## Clean up (python dependencies, downloaded infrastructure code)
	rm -f .coverage
	rm -rf .filesystem
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf $(VENV_DIR)


clean-dist:    ## Clean up python distribution directories
	rm -rf dist/ build/
	rm -rf code/*.egg-info


.PHONY: usage install tests-unit build clean clean-dist