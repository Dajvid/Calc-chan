PROJ = CChan
INT = python3
SRC = /src/
DOC = ../doc

all: ;

pack:

clean:
	rm -rf __pycache__

test:
	$(INT) -m unittest $(PROJ)Mathlib_tests.py

doc: Doxyfile
	rm -rf $(DOC)
	mkdir $(DOC)
	cd $(DOC) && doxygen ..$(SRC)/$<

run:
	$(INT) $(PROJ)Gui.py

profile:

.PHONY: all clean test run
