import glob, os, sys
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
os.chdir("../ebisu_uni_ge/")

def neoEntry(entry):
    if 'x' in entry: ##if date
        return 'entry'
    elif 'x' in entry: ##if datetime
        return 'entry'
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
