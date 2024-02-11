#! /usr/bin/env make
VENV_BIN ?= python3 -m venv
PIP_CMD ?= pip3

VENV_DIR ?= venv

VENV_ACTIVATE = $(VENV_DIR)/bin/activate

VENV_RUN = . $(VENV_ACTIVATE)

# Application path
APP_ROOT_PATH := ./sdk
UNIT_TESTS_PATH := ./tests/unit


usage:    ## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/:.*##\s*/##/g' | awk -F'##' '{ printf "%-40s %s\n", $$1, $$2 }'


$(VENV_ACTIVATE): setup.py
	test -d $(VENV_DIR) || $(VENV_BIN) $(VENV_DIR)
	$(VENV_RUN); $(PIP_CMD) install --upgrade pip setuptools wheel plux
	touch $(VENV_ACTIVATE)


venv: $(VENV_ACTIVATE)    ## Create a new (empty) dev virtual environment


# Install ONLY dev libraries
install: venv    ## Install all dependencies for dev environment
	$(VENV_RUN); $(PIP_CMD) install -r ${APP_ROOT_PATH}/requirements.txt
	$(VENV_RUN); $(PIP_CMD) install -r ${UNIT_TESTS_PATH}/requirements.txt


tests-unit: venv    ## Run the unit tests
	$(VENV_RUN); export PYTHONPATH=${APP_ROOT_PATH} \
	&& pytest --cov-report term-missing --cov-config=.coveragerc --cov=${APP_ROOT_PATH} ${UNIT_TESTS_PATH} -s -vv
