PROJ = CChan
INT = python3
SRC = /src/

all: ;

pack:

clean:
	rm -r $(SRC)__pycache__

test:
	$(INT) -m unittest $(PROJ)Mathlib_tests.py

doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc
	cd ../doc && doxygen ..$(SRC)/$<

run:
	$(INT) $(PROJ)Gui.py

profile: