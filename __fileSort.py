# import urllib.request, json
from module import json2py, py2json
from random import sample, random
from module.connectPostgreSQL import database
from module.import_tankerkoenig import tankerkoenig2sql
import module.file_management as fm

from datetime import datetime
from datetime import timedelta
import time, sys, os, exifread

# os.chdir("C:\\Users\\Konrad\\Dropbox\\Versicherung\\Haftpflicht\\DEVK\\")
os.chdir("C:\\Users\\Konrad\\Desktop\\")
print(os.getcwd())
#
# files_list = fm.get_files(os.getcwd())
# [print("["+str(entry)+"]", files_list[entry], ) for entry in range( len(files_list) )]
#
# type_list = [".png", ".pdf"]
#
# for tl in type_list:
#     print(any( [tl in fl for fl in files_list] ) )

drcty = fm.drcty(orig = os.getcwd())

print(drcty.files)

# print(drcty.get_tags())

drcty.types = [
    ".bmp", ".png", ".jpg", ".jpeg", ".gif", ## pictures
    # ".xcf", ## editor
    # ".eps", ".svg", ## vector
    # ".raw", ".tiff", ".dng", ".orf", ".heic", ## raw-pictures
    ".mov", ".mp4" ## movies
    ]
# print(drcty.types)
# print(drcty.orig, drcty.dest)

# print(drcty.move_all())
print(drcty.types)
print(drcty.get_tags())

# for item in drcty.get_tags():
#     try:
#         print(
#             item["Image Make"],
#             item["Image Model"],
#             [(i, item[i]) for i in item if "Date" in i])
#     except:
#         pass

# print(drcty.model, drcty.make)
# print(drcty.model, drcty.make, drcty.dt_min, drcty.dt_max)

# f = open("2018_11_01 18_34 Office Lens (5).jpg", 'rb')
# x = exifread.process_file(f)
# print(x.keys())

# tags = {}
# with open("2018_11_01 18_34 Office Lens (5).jpg", 'rb') as f_jpg:
#     tags = exifread.process_file(f_jpg)
#     # print (tags['Image Make'])
#     # print (tags['Image Model'])
#
# print("Hier kommen die Tags:")
# [print(tag) for tag in tags]
#
# for tag in tags.keys():
#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#         print("Key: %s, value %s" % (tag, tags[tag]))
#
#
#
# # import PIL.Image
# import ExifTags
# img = Image.open("2018_11_01 18_34 Office Lens (5).jpg")
# exif_data = img._getexif()
#
# exif = {
#     ExifTags.TAGS[k]: v
#     for k, v in img._getexif().items()
#     if k in PIL.ExifTags.TAGS
# }
#
# print(exif_data)
# print(exif)
#
# from PIL.ExifTags import TAGS
# from PIL import Image
#
# def get_exif(filename):
#     image = Image.open(filename)
#     image.verify()
#     return image._getexif()
#
# # print("tags", exif)
#
# def get_labeled_exif(exif):
#     labeled = {}
#     for (key, val) in exif.items():
#         labeled[TAGS.get(key)] = val
#
#     return labeled
#
# exif = get_exif("2018_11_01 18_34 Office Lens (5).jpg")
# labeled = get_labeled_exif(exif)
# print("tags",labeled)
#
# from PIL import Image
# from PIL.ExifTags import TAGS
#
# def get_exif():
#   i = Image.open('IMG_20180908_212627.jpg')
#   info = i._getexif()
#   return {TAGS.get(tag): value for tag, value in info.items()}
#
# print(get_exif())
