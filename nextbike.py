import time, glob, os, sys, urllib, shutil
from zipfile import ZipFile
from pathlib import Path
# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time
current = datetime.now()

from random import sample, randint, random

# import urllib.request, json
# from module.connectPostgreSQL import database
# from module.import_tankerkoenig import tankerkoenig2sql
import module.read.pi as rpi
from module import json2py, py2json

# os.chdir("../ebisu_uni_gear/")
# # save_file = '../nextbike/nextbike_'+f'{current:%Y%m%d}'+'.py' #'../nextbike/{%Y-%m-%d %H:%M:%S%z}'.format(current)
# # str_dtime = f'{current:%Y-%m-%d %H:%M:%S%z}'
# save_file = '../nextbike/nextbike_'+f'{current:%Y%m%d%H%M%S}'+'UTC.py' #'../nextbike/{%Y-%m-%d %H:%M:%S%z}'.format(current)
# details_file = '../details.json'

details_file = 'details.json'

strftime('%Y-%m-%d-%H:%M:%S')

save_file = 'nextbike_' + current.strftime('%Y-%m-%d_%H-%M-%S%z') + '.py'
# save_file = 'nextbike/nextbike_'+ current.strftime("%Y%m%d") +'.py'
# str_dtime = current.strftime("%Y-%m-%d %H:%M:%S%z")

def search_dict_in_list(input_list = [], search = None):
    for line in range(len(input_list)):
        try:
            if isinstance(input_list[line][search], int):
                return line
            else:
                pass
        except:
            pass
    return None

api_url = 'https://api.nextbike.net/maps/nextbike-live.json'


details_json = json2py(details_file)
json_line = search_dict_in_list(input_list = details_json, search = 'nextbike')
if json_line is None:
    details_dict = {'nextbike': 0}
else:
    details_dict = details_json[json_line]


if details_dict['nextbike'] < 1:
    print('run')

    # api_file = urllib.URLopener()
    urllib.request.urlretrieve(api_url, save_file)
    #
    # try:
    #     legacy = json2py(save_file)
    # except:
    #     legacy = []
    #
    # legacy.append({
    #     'datetime_utc': str_dtime,
    #     # 'response': {} #
    #     'response': json2py(api_url)
    #     })
    #
    # py2json(legacy, save_file)
    # details_dict['nextbike'] = randint(1, 2)
    details_dict['nextbike'] = randint(10, 20)

else:
    details_dict['nextbike'] = details_dict['nextbike'] - 1


try:
    details_json[json_line] = details_dict
except:
    details_json.append(details_dict)

py2json(details_json, details_file)
