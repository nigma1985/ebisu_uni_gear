import glob, os, sys, psycopg2
from zipfile import ZipFile
from pathlib import Path
from psycopg2 import Error

from module.connectPostgreSQL import database, dict2sql, getQuery, insertRow
from module.import_tankerkoenig import tankerkoenig2sql
from module import json2py, py2json

# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time

from random import sample, randint, random
start_time = time.mktime(datetime.now().timetuple())

# os.chdir("/home/pi/ebisu_uni_gear/")
# os.chdir("../ebisu_uni_gear/")
# details = '../details.json'

details = 'details.json'
details = json2py(details)

print('details', details)
postgres = []
for d in details:
    try:
        # if d['provider'] == 'PostgreSQL' and d['host'] == 'localhost':
        if d['provider'] == 'PostgreSQL':
            postgres.append(d)
        else:
            pass
    except:
        pass

if len(postgres) > 0:
    postgres = postgres[0]
else:
    pass

# print(postgres, postgres['host'], postgres['password'])

ebisu = database(
    db_type=None,
    port=postgres['port'],
    host=postgres['host'],
    user=postgres['user'],
    password=postgres['password'],
    dbname=postgres['database'])


# Find all views with name "v_coordinates_*"
table_name = []
for table in ebisu.getViews():
    # print(y)
    if 'v_coordinates_' in table and 'v_coordinates_all' not in table:
        table_name.append(table)
print(table_name)


# random call view from database
table_name = sample(table_name, 1)[0]
print(table_name)

# get 1000 rows from view
sql_data = ebisu.getSQL('''
    SELECT
        a.latitude,
        a.longitude,
        a.prio::FLOAT / (SELECT MAX(b.prio) FROM {} AS b WHERE a."user" = b."user"),
        a.last_visit,
        a."user"
    FROM
        {} AS a'''.format(table_name, table_name))
try:
    sql_data = sample(sql_data, 1000)
except:
    pass
print(sql_data)


for row in sql_data:
    insertRow(
        database = ebisu,
        schema_name = 'public',
        table_name = 'tab_coordinates_all',
        listNames = ['latitude', 'longitude', 'prio', 'last_visit', 'user', 'table'],
        listValues = [row[0], row[1], row[2], row[3], row[4], table_name[14:]],
        listWhere = ['latitude', 'longitude', 'user', 'table'],
        listTypes = ['FLOAT', 'FLOAT', 'FLOAT', 'TIMESTAMPTZ', 'TEXT', None])
