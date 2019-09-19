# import urllib.request, json
from module import json2py, py2json
from random import sample, random
from module.connectPostgreSQL import database
from module.import_tankerkoenig import tankerkoenig2sql
import module.file_management as fm

from datetime import datetime
from datetime import timedelta
import time, sys, os

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

drcty.types = [
    ".bmp", ".png", ".jpg", ".gif", ## pictures
    # ".xcf", ## editor
    # ".eps", ".svg", ## vector
    # ".raw", ".tiff", ".dng", ".orf", ".heic", ## raw-pictures
    ".mov", ".mp4" ## movies
    ]
print(drcty.types)
print(drcty.orig, drcty.dest)

print(drcty.move_all())
