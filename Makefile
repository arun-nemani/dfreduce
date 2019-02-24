# Makefile for dfreduce

# PHONY prevents issues with files/folders with the same names as makefile commands
.PHONY: help init venv notebook clean models datapull model-train model-results tests aws all load-models
VIRTUAL_ENV=venv
export VIRTUALENV_PATH := $(abspath ${VIRTUAL_ENV})

.DEFAULT: help
help:
	@echo "make venv --------------- Setup virtual Python3 environment ($(VIRTUAL_ENV))
	@echo "make init --------------- Install requirements in ($(VIRTUAL_ENV))"
	@echo "make notebook ----------- Create jupyter notebook kernel in ($(VIRTUAL_ENV))"
	@echo "make clean -------------- Remove ($(VIRTUAL_ENV)) and installed subcomponents"

venv:
	python3 -m virtualenv $(VIRTUAL_ENV)
	@echo "-----"
	@echo "Environment ($(VIRTUAL_ENV)) installed in $(VIRTUALENV_PATH)"

init:
	pip install -r requirements.txt
	pip install ipykernel
	@echo "-----"
	@echo "dfreduce package installed"

notebook:
	ipython kernel install --user --name=dfreduce

clean:
	rm -rf $(VIRTUAL_ENV)
	jupyter kernelspec remove dfreduce
	@echo "-----"
	@echo "Deleted ($(VIRTUAL_ENV)) with dfreduce package"

tests:
	python3 tests/datapull_test.py
	python3 tests/model-train_test.py
	python3 tests/model-results_test.py

