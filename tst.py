import os
# from db import database
from module import json2py
from module.connectPostgreSQL import database
import module.dict2sql as d2s
import module.list2sql as l2s

os.chdir("../ebisu_uni_gear/")

## input
ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

print(ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad']))
