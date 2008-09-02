#!/usr/bin/env python

"""
Utility to adjust the EXIF timestamps in JPEG files by a constant offset.

Requires Benno's pexif library: http://code.google.com/p/pexif/

-- Andrew Baumann <andrewb@inf.ethz.ch>, 20080716
"""

import sys
from pexif import JpegFile, EXIF_OFFSET
from datetime import timedelta, datetime
from optparse import OptionParser

DATETIME_EMBEDDED_TAGS = ["DateTimeOriginal", "DateTimeDigitized"]
TIME_FORMAT = '%Y:%m:%d %H:%M:%S'

def parse_args():
    p = OptionParser(usage='%prog hours file.jpg...',
           description='adjusts timestamps in EXIF metadata by given offset')
    options, args = p.parse_args()
    if len(args) < 2:
        p.error('not enough arguments')
    try:
        hours = int(args[0])
    except:
        p.error('invalid time offset, must be an integral number of hours')
    return hours, args[1:]

def adjust_time(primary, delta):
    def adjust_tag(timetag, delta):
        dt = datetime.strptime(timetag, TIME_FORMAT)
        dt += delta
        return dt.strftime(TIME_FORMAT)

    if primary.DateTime:
        primary.DateTime = adjust_tag(primary.DateTime, delta)

    embedded = primary[EXIF_OFFSET]
    if embedded:
        for tag in DATETIME_EMBEDDED_TAGS:
            if embedded[tag]:
                embedded[tag] = adjust_tag(embedded[tag], delta)

def main():
    hours, files = parse_args()
    delta = timedelta(hours=hours)

    for fname in files:
        try:
            jf = JpegFile.fromFile(fname)
        except (IOError, JpegFile.InvalidFile):
            type, value, traceback = sys.exc_info()
            print >> sys.stderr, "Error reading %s:" % fname, value
            return 1

        exif = jf.get_exif()
        if exif:
            primary = exif.get_primary()
        if exif is None or primary is None:
            print >> sys.stderr, "%s has no EXIF tag, skipping" % fname
            continue

        adjust_time(primary, delta)

        try:
            jf.writeFile(fname)
        except IOError:
            type, value, traceback = sys.exc_info()
            print >> sys.stderr, "Error saving %s:" % fname, value
            return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
