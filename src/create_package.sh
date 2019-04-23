#!/bin/bash

# create installator directory
mkdir -p ../install/cchan/usr/local/bin
mkdir -p ../install/cchan/usr/share/cchan

# copy application files
cp CChanGui.py ../install/cchan/usr/share/cchan
cp CChanParser.py ../install/cchan/usr/share/cchan
cp CChanMathlib.py ../install/cchan/usr/share/cchan

ln -sf /usr/share/cchan/CChanGui.py ../install/cchan/usr/local/bin/cchan

chmod +x ../install/cchan/usr/share/cchan/CChanGui.py
dpkg-deb --build ../install/cchan
