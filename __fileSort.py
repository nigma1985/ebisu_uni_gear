# import urllib.request, json
from module import json2py, py2json
from random import sample, random
from module.connectPostgreSQL import database
from module.import_tankerkoenig import tankerkoenig2sql
import module.file_management as fm

from datetime import datetime
from datetime import timedelta
import time, sys, re, os, exifread

# os.chdir("C:\\Users\\Konrad\\Dropbox\\Versicherung\\Haftpflicht\\DEVK\\")
os.chdir("C:\\Users\\Konrad\\Desktop\\")
print(os.getcwd())
#
files_list = fm.get_files(os.getcwd())
# [print("["+str(entry)+"]", files_list[entry], ) for entry in range( len(files_list) )]
#
type_list = [".png", ".pdf"]
#
for tl in type_list:
    print(any( [tl in fl for fl in files_list] ) )

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

drcty.move_all()

################################################################################

tst_file = "IMG-20180906-WA0006.jpeg"
tst = fm.file(directory = os.getcwd(), element = tst_file, types = drcty.types)
print(tst.element, tst.make, tst.model, min(tst.atime, tst.mtime, tst.ctime))

lst = [ tst.tags[entry] for entry in tst.tags if "Date" in entry]

print(tst_file, fm.find_date(string = tst_file))
print(tst.date_from_name, tst.exif_min_date, tst.exif_max_date)
