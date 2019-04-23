PROJ = CChan
INT = python3
SRC = /src/
DOC = ../doc

all: ;

pack: doc xhanak34_xhavli46_xjakub34_xsedla1d.zip

xhanak34_xhavli46_xjakub34_xsedla1d.zip:
	mkdir -p ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo
	cp --archive ../../Calc-chan/. ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo
	mv ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo/doc ../../xhanak34_xhavli46_xjakub34_xsedla1d/doc
	mv ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo/install ../../xhanak34_xhavli46_xjakub34_xsedla1d/install
	rm -rf ../../xhanak34_xhavli46_xjakub34_xsedla1d/install/cchan
	zip -r ../../$@ ../../xhanak34_xhavli46_xjakub34_xsedla1d/*

clean:
	rm -rf __pycache__ ../install/cchan

test:
	$(INT) -m unittest $(PROJ)Mathlib_tests.py

doc: Doxyfile
	rm -rf $(DOC)
	mkdir $(DOC)
	doxygen $<

run:
	$(INT) $(PROJ)Gui.py

profile:

installer: CChanMathlib.py CChanParser.py create_package.sh
	bash create_package.sh

.PHONY: all clean test run
