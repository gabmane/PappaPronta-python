PYTHON=python
TESTDIR=test

all: tests

tests:
	$(PYTHON) $(TESTDIR)/**/*_test.py
