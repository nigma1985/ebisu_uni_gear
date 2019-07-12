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

# print(postgres, postgres['host'], postgres['password'])

ebisu = database(db_type=None, port=postgres['port'], host=postgres['host'], user=postgres['user'], password=postgres['password'], dbname=postgres['database'])
















lst = '../list.json'
prcs = '../prices.json'
dtls = '../detail.json'

path = lst
tankerkoenig = json2py(jsonPath = path)

# print(path, '.php' in path)
result = {}
if 'list.' in path:
    # print('list')
    result['method'] = 'list.php'
    for i in tankerkoenig:
        if i == 'stations':
            result['results'] = tankerkoenig[i]
        else:
            result[i] = tankerkoenig[i]
#
# elif 'prices.' in path:
#     result['method'] = 'prices.php'
#     tmp_list = []
#     for i in tankerkoenig:
#         if i == 'prices':
#             # result['stations'] = tankerkoenig[i]
#             for j in tankerkoenig[i]:
#                 tankerkoenig[i][j]['id'] = j
#                 tmp_list.append(tankerkoenig[i][j])
#                 # print(j, tankerkoenig[i][j])
#             result['results'] = tmp_list
#         else:
#             result[i] = tankerkoenig[i]
#
# elif 'detail.' in path:
#     # print('details')
#     result['method'] = 'detail.php'
#     for i in tankerkoenig:
#         if i == 'station':
#             result['results'] = [tankerkoenig[i]]
#         else:
#             result[i] = tankerkoenig[i]
# elif 'complaint.php' in path:
#     result['method'] = 'complaint.php' ## not implemented
# else:
#     result['method'] = None

print('tankerkoenig', len(tankerkoenig), tankerkoenig)
for i in tankerkoenig:
    print(type(tankerkoenig[i]), i, tankerkoenig[i])

print('result', len(result), result)
for i in result:
    print(type(result[i]), i, result[i])

# print(result['results'][1])

for k in result['results']:
    k['situation'] = []
    tmp_list = {}
    #     tmp_list[k] = result['results'][k]
    #     del result['results'][k]
    # result['results']['situation'].append(tmp_list)
#
# print('result', len(result), result)
# for i in result:
#     print(type(result[i]), i, result[i])

# lst: ok, licence, data, status, stations [list]
# prcs: ok, licence, data, prices [dict]
# dtls: ok, licence, data, status, station [dict]

# tankerkoenig2sql(
#     tankerkoenig_reply = result,
#     db_name = ebisu,
#     # father_table = None, father_id = None,
#     table_name = 'tankerkoenig',
#     addNames = ['utc_datetime'],
#     addValues = [datetime.utcnow()],
#     user = 'John.Doe@test.tst'
#     )
#
#
# # print(type(ebisu.getSQL('SELECT COUNT(*) FROM public."SuperStore";')))
