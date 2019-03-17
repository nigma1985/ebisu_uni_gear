import os
# from db import database
from module import json2py
from module.dict2sql import dict2sql
from module.list2sql import list2sql

os.chdir("../ebisu_uni_gear/")

## input
activities = json2py(jsonPath = 'input/activities_20151126.json')
ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

print(len(activities))
print(activities[0])
## convert

## output

## write
