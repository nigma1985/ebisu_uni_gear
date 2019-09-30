# # import urllib.request, json
# from module import json2py, py2json
# from random import sample, random
# from module.connectPostgreSQL import database
# from module.import_tankerkoenig import tankerkoenig2sql
#
# from datetime import datetime
# from datetime import timedelta
# import time, sys
#
#
#
#
#
# details = '../details.json'
# details = json2py(details)
#
# print('details', details)
# postgres = []
# for d in details:
#     if d['provider'] == 'PostgreSQL' and d['host'] == 'localhost':
#         postgres.append(d)
#     else:
#         pass
#
# if len(postgres) > 0:
#     postgres = postgres[1]
# else:
#     pass
#
# # print(postgres, postgres['host'], postgres['password'])
#
# ebisu = database(db_type=None, port=postgres['port'], host=postgres['host'], user=postgres['user'], password=postgres['password'], dbname=postgres['database'])
#
#
# liste = ['Ich', 'Du', 'Er', 'Sie', 'Es', None]
# # print([i.lower() for i in liste])
# print([i.upper() if i is not None else None for i in liste])

tst = ['Ich', 123, None]
x, y, z = tst
print("print:", x, y, z)
