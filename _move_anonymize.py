import glob, os, sys, re
from zipfile import ZipFile
from pathlib import Path

# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time
from module import json2py, py2json

from random import sample, randint
start_time = time.mktime(datetime.now().timetuple())

# os.chdir("/home/pi/ebisu_uni_gear/")
os.chdir("../ebisu_uni_gear/")

def neoEntry(entry):
    if len(entry) in (16,20) and re.search("(((19|20)([2468][048]|[13579][26]|0[48])|2000)0229|((19|20)[0-9]{2}(0[469]|11)(0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}(0[13578]|1[02])(0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}02(0[1-9]|1[0-9]|2[0-8])))", entry): ##if date
        return datetime.strptime(entry, '%Y%m%dT%H%M%S%z').strftime("%Y-%m-%d %H:%M:%S%z")
    elif len(entry) == 8 and re.search("(((19|20)([2468][048]|[13579][26]|0[48])|2000)0229|((19|20)[0-9]{2}(0[469]|11)(0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}(0[13578]|1[02])(0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}02(0[1-9]|1[0-9]|2[0-8])))", entry): ##if date
            return datetime.strptime(entry, '%Y%m%d').strftime("%Y-%m-%d")
    elif 'x' in entry: ##if datetime TZ
        return 'entry'
    elif 'x' in entry: ##if Aileen
        return 'entry'
    elif 'x' in entry: ##if Sascha
        return 'entry'
    elif 'x' in entry: ##if Dominik
        return 'entry'
    else:
        return entry

def neoData(data):
    rtn = None
    if isinstance(data, (list, tuple)):
        rtn = []
        for item in data:
            rtn.append(neoData(item))
    elif isinstance(data, dict):
        rtn = {}
        for entry in data:
            rtn[entry] = neoData(data[entry])
    elif isinstance(data, str):
        rtn = neoEntry(data)
    else:
        rtn = data

    return rtn





file = '../storyline.json'
anon = '../anon_storyline.json'

orig = json2py(file)

py2json(neoData(orig), anon)
