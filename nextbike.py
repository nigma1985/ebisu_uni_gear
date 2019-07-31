import time, glob, os, sys
from zipfile import ZipFile
from pathlib import Path
# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time

from random import sample, randint, random

# import urllib.request, json
# from module.connectPostgreSQL import database
# from module.import_tankerkoenig import tankerkoenig2sql
import module.read.pi as rpi
from module import json2py, py2json

# os.chdir("/home/pi/ebisu_uni_gear/")
os.chdir("../ebisu_uni_gear/")

def search_dict_in_list(input_list = [], search = None):
    for line in range(len(input_list)):
        try:
            if input_list[line][search]:
                return line
            else:
                pass
        except:
            pass
    return None

api_url = 'https://api.nextbike.net/maps/nextbike-live.json'
current = datetime.now()

details_file = '../details.json'
details_json = json2py(details_file)
json_line = search_dict_in_list(input_list = details_json, search = 'nextbike')
if json_line is None:
    details_dict = {'nextbike': 0}
else:
    details_dict = details_json[json_line]

# print(details_dict)

if details_dict['nextbike'] < 1:
    print('run')

    save_file = '../nextbike/nextbike_'+f'{current:%Y%m%d}'+'.py' #'../nextbike/{%Y-%m-%d %H:%M:%S%z}'.format(current)
    str_dtime = f'{current:%Y-%m-%d %H:%M:%S%z}'

    try:
        legacy = json2py(save_file)
    except:
        legacy = []

    legacy.append({
        'datetime_utc': str_dtime,
        'response': json2py(api_url)
        })

    py2json(legacy, save_file)
    details_dict['nextbike'] = randint(10, 20)
else:
    print('sleep', details_dict['nextbike'])
    details_dict['nextbike'] = details_dict['nextbike'] - 1

try:
    details_json[json_line] = details_dict
except:
    details_json.append(details_dict)
py2json(details_json, details_file)
