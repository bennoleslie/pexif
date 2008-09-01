#!/usr/bin/env python

from pexif import JpegFile
import sys

usage = """Usage: dump_exif.py filename.jpg"""

if len(sys.argv) != 2:
    print >> sys.stderr, usage
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    ef.dump()
except IOError:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error opening file:", value
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print >> sys.stderr, "Error opening file:", value
