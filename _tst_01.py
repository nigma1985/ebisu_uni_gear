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
    postgres = postgres[1]
else:
    pass

ebisu = database(db_type=None, port=postgres['port'], host=postgres['host'], user=postgres['user'], password=postgres['password'], dbname=postgres['database'])
















lst = '../list.json'
prcs = '../prices.json'
dtls = '../detail.json'

path = lst
tankerkoenig = json2py(jsonPath = path)


result = {}
if 'list.' in path:
    result['method'] = 'list.php'
    for i in tankerkoenig:
        if i == 'stations':
            result['results'] = tankerkoenig[i]
        else:
            result[i] = tankerkoenig[i]

elif 'prices.' in path:
    result['method'] = 'prices.php'
    tmp_list = []
    for i in tankerkoenig:
        if i == 'prices':
            for j in tankerkoenig[i]:
                tankerkoenig[i][j]['id'] = j
                tmp_list.append(tankerkoenig[i][j])
            result['results'] = tmp_list
        else:
            result[i] = tankerkoenig[i]

elif 'detail.' in path:
    # print('details')
    result['method'] = 'detail.php'
    for i in tankerkoenig:
        if i == 'station':
            result['results'] = [tankerkoenig[i]]
        else:
            result[i] = tankerkoenig[i]
elif 'complaint.php' in path:
    result['method'] = 'complaint.php' ## not implemented
else:
    result['method'] = None

print('tankerkoenig', len(tankerkoenig), tankerkoenig)
for i in tankerkoenig:
    print(type(tankerkoenig[i]), i, tankerkoenig[i])

print('result', len(result), result)
for i in result:
    print(type(result[i]), i, result[i])


def sub_table(super_table = {}, replace = '', find = ()):
    for line in range(len(super_table)):
        super_table[line][replace] = {}
        for key in [k for k in super_table[line]]:
            if key in find:
                super_table[line][replace][key] = super_table[line][key]
                del super_table[line][key]
            else:
                pass
    return super_table

result['results'] = sub_table(super_table = result['results'], replace = 'station_values', find = ('dist', 'diesel', 'e5', 'e10', 'isOpen', 'status'))
result['results'] = sub_table(super_table = result['results'], replace = 'station_location', find = ('id', 'name', 'brand', 'street', 'place', 'lat', 'lng', 'houseNumber', 'postCode', 'wholeday'))

# print(result)


tankerkoenig2sql(
    tankerkoenig_reply = result,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'tankerkoenig',
    addNames = ['utc_datetime'],
    addValues = [datetime.utcnow()],
    user = 'John.Doe@test.tst'
    )
