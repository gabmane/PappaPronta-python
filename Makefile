PYTHON=python
TESTDIR=test

all: tests

tests:
	for f in $(TESTDIR)/**/*_test.py; do\
		echo "Testing $$f:";\
		$(PYTHON) $$f;\
	done
