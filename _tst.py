# import urllib.request, json
from module import json2py, py2json
from random import sample, random
from module.connectPostgreSQL import database
from module.import_tankerkoenig import tankerkoenig2sql

from datetime import datetime
from datetime import timedelta
import time, sys





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
    postgres = postgres[0]
else:
    pass

print(postgres, postgres['host'], postgres['password'])

ebisu = database(db_type=None, port=postgres['port'], host=postgres['host'], user=postgres['user'], password=postgres['password'], dbname=postgres['database'])











##############################################
#
# if dict then key + value[key]
#
# add date
#






lst = '../list.json'
prcs = '../prices.json'
dtls = '../detail.json'

path = lst
tankerkoenig = json2py(jsonPath = path)

if 'list.php' in path:
    method = 'list.php'
elif 'prices.php' in path:
    method = 'prices.php'
elif 'detail.php' in path:
    method = 'detail.php'
elif 'complaint.php' in path:
    method = 'complaint.php' ## not implemented
else:
    method = None

tankerkoenig2sql(
    tankerkoenig_reply = tankerkoenig,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'tankerkoenig',
    addNames = ['method', 'utc_datetime'],
    addValues = [method, datetime.utcnow()],
    user = 'John.Doe@test.tst'
    )
