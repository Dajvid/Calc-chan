PROJ = CChan
INT = python3
SRC = /src/
DOC = ../doc

all: ;

pack: doc installer xhanak34_xhavli46_xjakub34_xsedla1d.zip


xhanak34_xhavli46_xjakub34_xsedla1d.zip:
	rm -rf ../../xhanak34_xhavli46_xjakub34_xsedla1d
	rm -rf ../../$@
	mkdir -p ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo
	cp --archive ../../Calc-chan/. ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo
	mv ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo/doc ../../xhanak34_xhavli46_xjakub34_xsedla1d/doc
	mv ../../xhanak34_xhavli46_xjakub34_xsedla1d/repo/install ../../xhanak34_xhavli46_xjakub34_xsedla1d/install
	rm -rf ../../xhanak34_xhavli46_xjakub34_xsedla1d/install/cchan
	zip -r ../../$@ ../../xhanak34_xhavli46_xjakub34_xsedla1d/*
	rm -rf ../../xhanak34_xhavli46_xjakub34_xsedla1d

clean:
	rm -rf __pycache__
	rm -rf ../install/cchan/usr/share/cchan/*.py
	rm -rf ../install/cchan/usr/local/bin/cchan

test:
	$(INT) -m unittest $(PROJ)Mathlib_tests.py

doc: Doxyfile
	rm -rf $(DOC)
	mkdir $(DOC)
	doxygen $<

run:
	$(INT) $(PROJ)Gui.py

profile: ;

installer: CChanMathlib.py CChanParser.py create_package.sh
	bash create_package.sh

.PHONY: all pack xhanak34_xhavli46_xjakub34_xsedla1d.zip clean test doc run profile installer
