import glob, os
# import module.read.pi as rpi
# from db import database
from module import json2py, removeFile
from module.connectPostgreSQL import database
from module.import_moves import move2sql

os.chdir("../ebisu_uni_gear/")

# ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')
# ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

x = ebisu.getSQL('''SELECT id, CAST ( duration AS FLOAT ) AS duration FROM activities;''')

print(x)
