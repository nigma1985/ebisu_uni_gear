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

# print(drcty.types)
# print(drcty.get_tags())

# print(drcty.model, drcty.model)


tst_file = "IMG-20180906-WA0006.jpeg"
tst = fm.file(directory = os.getcwd(), element = tst_file, types = drcty.types)
print(tst.element, tst.make, tst.model, min(tst.atime, tst.mtime, tst.ctime))
print(type(tst.element), type(tst.make), type(tst.model), type(tst.atime), type(tst.mtime), type(tst.ctime))

# import dateparser
# from dateparser.search import search_dates


# entry for entry in tst.tags if 'date' in entry


print('tags', tst.tags)


lst = [ tst.tags[entry] for entry in tst.tags if "Date" in entry]

# https://regex101.com/
# http://www.regexlib.com/Search.aspx?k=yyyy-mm-dd&c=-1&m=-1&ps=20
# IMG-20180906-WA0006.jpeg
# (0x0132) ASCII=2018:09:06 21:42:59 @ 171
# (0x9004) ASCII=2018:09:06 20:29:09 @ 613
# (0x9003) ASCII=2018:09:06 20:29:09 @ 641

# ((\d{2}(([02468][048])|([13579][26]))\W?((((0?[13578])|(1[02]))\W?((0?[1-9])|([1-2][0-9])|(3[01])))|(((0?[469])|(11))\W?((0?[1-9])|([1-2][0-9])|(30)))|(0?2\W?((0?[1-9])|([1-2][0-9])))))|(\d{2}(([02468][1235679])|([13579][01345789]))\W?((((0?[13578])|(1[02]))\W?((0?[1-9])|([1-2][0-9])|(3[01])))|(((0?[469])|(11))\W?((0?[1-9])|([1-2][0-9])|(30)))|(0?2\W?((0?[1-9])|(1[0-9])|(2[0-8]))))))(.?(((0?[1-9])|(1[0-9])|(2[0-3]))\W?([0-5][0-9])((\s)|(\W?([0-5][0-9])))?))?
regex_time = "((0[0-9]|1[0-9]|2[0-3]\\W?[0-5][0-9])(\\W?[0-5][0-9])?)"
regex_date = "(((19|20)([2468][048]|[13579][26]|0[48])|2000)\\W?02\\W?29|((19|20)[0-9]{2}\\W?(0[469]|11)\\W?(0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}\\W?(0[13578]|1[02])\\W?(0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}\\W?02\\W?(0[1-9]|1[0-9]|2[0-8])))"
# (((\d{4}\W?((0[13578]\W?|1[02]\W?)(0[1-9]|[12]\d|3[01])|(0[13456789]\W?|1[012]\W?)(0[1-9]|[12]\d|30)|02\W?(0[1-9]|1\d|2[0-8])))|((([02468][048]|[13579][26])00|\d{2}([13579][26]|0[48]|[2468][048])))\W?02\W?29)){0,10}
regex = "\\D?({}\\D?({})?)\\D?".format(regex_date, regex_time)

# [ tst.tags[entry] if 'date' in entry for entry in tst.tags ]
print('lst', lst)

for item in lst:
    found = re.search(regex, str(item), re.IGNORECASE)
    if found:
        print(found.group(1))
    else:
        "empty"
