"""
An example showing how to set the Image title on a jpeg file.
"""

import pexif

# Modify  the exif in a file
img = pexif.JpegFile.fromFile("test/data/rose.jpg")
img.exif.primary.ImageDescription =  "Hello world!"
img.writeFile("hello1.jpg")

# Add exif in a file
img = pexif.JpegFile.fromFile("test/data/noexif.jpg")
img.exif.primary.ImageDescription =  "Hello world!"
img.writeFile("hello2.jpg")

# Copy some exif field from one to another
primary_src = pexif.JpegFile.fromFile("test/data/rose.jpg").exif.primary
img_dst = pexif.JpegFile.fromFile("test/data/noexif.jpg")
primary_dst = img_dst.exif.primary
primary_dst.Model = primary_src.Model
primary_dst.Make = primary_src.Make

img_dst.writeFile("hello3.jpg")
