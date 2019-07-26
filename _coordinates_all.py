import glob, os, sys
from zipfile import ZipFile
from pathlib import Path
from module.connectPostgreSQL import database
from module.import_tankerkoenig import tankerkoenig2sql
from module import json2py, py2json

# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time

from random import sample, randint, random
start_time = time.mktime(datetime.now().timetuple())

# os.chdir("/home/pi/ebisu_uni_gear/")
os.chdir("../ebisu_uni_gear/")

details = '../details.json'
details = json2py(details)

print('details', details)
postgres = []
for d in details:
    if d['provider'] == 'PostgreSQL' and d['host'] == 'localhost':
        postgres.append(d)
    else:
        pass

if len(postgres) > 0:
    postgres = postgres[1]
else:
    pass

# print(postgres, postgres['host'], postgres['password'])

ebisu = database(db_type=None, port=postgres['port'], host=postgres['host'], user=postgres['user'], password=postgres['password'], dbname=postgres['database'])


# Find all views with name "v_coordinates_*"
xxx = []
for y in ebisu.getViews():
    # print(y)
    if 'v_coordinates' in y:
        xxx.append(y)
print(xxx)


# random call view from database
xxx = sample(xxx, 1)[0]
print(xxx)

# get 1000 rows from view
sql = ebisu.getSQL('''SELECT * FROM {}'''.format(xxx))
try:
    sql = sample(sql, 100)
except:
    pass
print(sql)

# summerize priority values
# send lat, long, priority and date with view name to table
