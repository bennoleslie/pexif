#!/usr/bin/env python
from pexif import JpegFile
import sys

usage = """Usage: setgps.py filename.jpg lat lng"""

if len(sys.argv) != 4:
    print >> sys.stderr, usage
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    ef.set_geo(float(sys.argv[2]), float(sys.argv[3]))
except IOError:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error opening file:", value
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error opening file:", value

try:
    ef.writeFile(sys.argv[1])
except IOError:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error saving file:", value

