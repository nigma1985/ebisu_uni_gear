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
os.chdir("C:\\Users\\Konrad\\Desktop\\tst_folder\\")
print(os.getcwd())
#
files_list = fm.get_files(os.getcwd())
# [print("["+str(entry)+"]", files_list[entry], ) for entry in range( len(files_list) )]
# #
# type_list = [".png", ".pdf"]
# #
# for tl in type_list:
#     print(any( [tl in fl for fl in files_list] ) )

drcty = fm.drcty(orig = os.getcwd(), types = [
    ".bmp", ".png", ".jpg", ".jpeg", ".gif", ## pictures
    ".xcf", ## editor
    ".eps", ".svg", ## vector
    ".raw", ".tiff", ".dng", ".orf", ".heic", ## raw-pictures
    ".mov", ".mp4", ".wmv", ## movies
    ".mp3", ".wma", ".ogg" ## audio
    ])

print(drcty.files)

# print(drcty.get_tags())
# drcty.types = [
#     ".bmp", ".png", ".jpg", ".jpeg", ".gif", ## pictures
#     ".xcf", ## editor
#     ".eps", ".svg", ## vector
#     ".raw", ".tiff", ".dng", ".orf", ".heic", ## raw-pictures
#     ".mov", ".mp4" ## movies
#     ]

# drcty.move_all()

################################################################################

# tst_file = "IMG-20180906-WA0006.jpeg"
# # tst_file = "2019-10-21"
# # tst_file = "2018_11_01 18_34 Office Lens (5).jpg"
# tst_file = "tst_20191024_diffdates"
# tst = fm.file(directory = os.getcwd(), element = tst_file, types = drcty.types)
# print(tst.element, tst.make, tst.model, min(tst.atime, tst.mtime, tst.ctime))
#
# # lst = [ tst.tags[entry] for entry in tst.tags if "Date" in entry ]
#
# # print(tst_file, fm.find_date(string = tst_file))
# # print(tst.date_from_name, tst.exif_min_date, tst.exif_max_date)

print(drcty._listDir())
print()
# print('lalal',
#     [tst._findDate_in_Dir(), type(tst._findDate_in_Dir())],
#     [tst.get_date().strftime('%Y-%m-%d'), type(tst.get_date())],
#     "|",
#     tst._findDate_in_Dir()   if   tst._findDate_in_Dir() is not None   else   tst.get_date().strftime('%Y-%m-%d')
#     )
# print('path: ', tst.get_path())

###############################################################################
print(" -- tst: one out of many -- for extracting singular atribute from directory of files")
tst_list = [None, "ich", None, "ich", None, "du", None, "ich", None, "ich", None]
tst_list_clean = fm.clean_list(tst_list)
print('list', tst_list_clean)
print('get_attr:', fm.get_attr(attr_list = tst_list_clean))
print('get_moda:', fm.get_moda(attr_list = tst_list_clean))
###############################################################################

###############################################################################
print(" -- tst: intervall? -- to determine weather files where created in a burst")
# tst_list = [None, 2, 4, 6, 8, 10, None]
# tst_list = [None, 2, 2, 2, 2, 2, 2]
tst_list = [None, 2, 3,  6, 7,  10, 11,  14, None]
tst_list_clean = fm.clean_list(tst_list)
print('get_regr:', fm.get_regr(attr_list = tst_list_clean))
###############################################################################

for elem in drcty.files:
    print(drcty.files[elem].tid, elem.strip(), "|",
        str(drcty.files[elem].make).strip() if drcty.files[elem].make else None,
        str(drcty.files[elem].model).strip() if drcty.files[elem].model else None)
    if drcty.files[elem].tid < 0:
        for e in drcty.files[elem].folder.files:
            print("|", drcty.files[elem].folder.files[e].tid, e.strip(), "|",
                str(drcty.files[elem].folder.files[e].make).strip() if drcty.files[elem].folder.files[e].make else None,
                str(drcty.files[elem].folder.files[e].model).strip() if drcty.files[elem].folder.files[e].model else None)
