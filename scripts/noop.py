#!/usr/bin/env python

from pexif import JpegFile
import sys

usage = """Usage: dump_exif.py filename.jpg out.jpg"""

if len(sys.argv) != 3:
    print >> sys.stderr, usage
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
except IOError:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error opening file:", value
    sys.exit(1)
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error opening file:", value
    sys.exit(1)

try:
    ef.writeFile(sys.argv[2])
except IOError:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error saving file:", value
    sys.exit(1)
