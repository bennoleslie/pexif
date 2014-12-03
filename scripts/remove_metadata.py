#!/usr/bin/env python
from pexif import JpegFile
import sys

usage = """Usage: remove_metadata.py filename.jpg"""

if len(sys.argv) != 4:
    print >> sys.stderr, usage
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    ef.remove_metadata(paranoid=True)
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
