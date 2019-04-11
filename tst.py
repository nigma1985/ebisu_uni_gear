# import glob, os
# # from db import database
# from module import json2py
# from module.connectPostgreSQL import database
# from module.import_moves import mact2sql
#
# ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')
# ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

x = 'text'
y = 'my %s'.format(x)

print(x, y)
