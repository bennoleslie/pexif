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
img.exif.primary.ImageDescription = "Hello world!"
img.exif.primary.ExtendedEXIF.UserComment = "a simple comment"
img.writeFile("hello2.jpg")

# Copy some exif field from one to another
primary_src = pexif.JpegFile.fromFile("test/data/rose.jpg").exif.primary
img_dst = pexif.JpegFile.fromFile("test/data/noexif.jpg")
primary_dst = img_dst.exif.primary
primary_dst.Model = primary_src.Model
primary_dst.Make = primary_src.Make
img_dst.writeFile("hello3.jpg")

# Copy entire exif from one to another (where there is no exif)
img_src = pexif.JpegFile.fromFile("test/data/rose.jpg")
img_dst = pexif.JpegFile.fromFile("test/data/noexif.jpg")
img_dst.import_exif(img_src.exif)
img_dst.writeFile("hello4.jpg")

# Copy entire exif from one to another (where there is exif)
img_src = pexif.JpegFile.fromFile("test/data/rose.jpg")
img_dst = pexif.JpegFile.fromFile("test/data/conker.jpg")
img_dst.import_exif(img_src.exif)
img_dst.writeFile("hello5.jpg")


# Remove metadata
img_dst = pexif.JpegFile.fromFile("test/data/rose.jpg")
img_dst.remove_metadata(paranoid=True)
img_dst.writeFile("hello6.jpg")
