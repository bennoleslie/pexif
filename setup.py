#!/usr/bin/env python

from distutils.core import setup

version = "0.15"

"""Setup script for pexif"""

setup (
    name = "pexif",
    version = version,
    description = "A module for editing JPEG EXIF data",
    long_description = "This module allows you to parse and edit the EXIF data tags in a JPEG image.",
    author = "Ben Leslie",
    author_email = "benno@benno.id.au",
    url = "http://www.benno.id.au/code/pexif/",
    license = "http://www.opensource.org/licenses/mit-license.php",
    py_modules = ["pexif"],
    scripts = ["scripts/dump_exif.py", "scripts/setgps.py", "scripts/getgps.py", "scripts/noop.py",
               "scripts/timezone.py", "scripts/remove_metadata.py"],
    platforms = ["any"],
    classifiers = ["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "License :: OSI Approved :: MIT License",
                   "Topic :: Multimedia :: Graphics"]
    )
