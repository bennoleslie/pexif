"""
An example showing how to set the Image title on a jpeg file.
"""

import pexif

# Modify the exif in a file
img = pexif.JpegFile.fromFile("test/data/rose.jpg")
img.get_exif().get_primary()[pexif.ImageDescription] =  "Hello world!"
img.writeFile("hello.jpg")

# Add exif to an image
img = pexif.JpegFile.fromFile("test/data/noexif.jpg")
exif = img.get_exif(create=True)
exif.get_primary(create=True)[pexif.ImageDescription] =  "Hello world!"
img.writeFile("hello2.jpg")

# Copy exif from one to another
img_src = pexif.JpegFile.fromFile("test/data/rose.jpg")
img_dst = pexif.JpegFile.fromFile("test/data/noexif.jpg")
primary_src = img_src.get_exif().get_primary()
primary_dst = img_dst.get_exif(create=True).get_primary(create=True)
for entry in primary_src.entries:
    if entry[0] in [pexif.ImageDescription, pexif.Make, pexif.Model]:
        primary_dst[entry[0]] = entry[2]

img_dst.writeFile("hello3.jpg")
