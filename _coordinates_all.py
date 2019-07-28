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
table_name = []
for table in ebisu.getViews():
    # print(y)
    if 'v_coordinates_' in table:
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

# summerize priority values
## done
data = []
for row in sql_data:
    data.append(
        {
            'latitude': row[0],
            'longitude': row[1],
            'prio': row[2],
            'last_visit': row[3],
            'user': row[4],
            'table': table_name[14:],
        }
    )

print(data)
# send lat, long, priority and date with view name to table
