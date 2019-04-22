PROJ = CChan
SRC = ./src/
INT = python3

all: ;

pack:

clean:
	rm -r $(SRC)__pycache__
test:
	$(INT) -m unittest $(SRC)$(PROJ)Mathlib_tests.py
doc:

run:
	$(INT) $(SRC)$(PROJ)Gui.py

profile: