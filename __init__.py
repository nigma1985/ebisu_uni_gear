import os
# from db import database
from module import json2py, database
import module.dict2sql as d2s
import module.list2sql as l2s

os.chdir("../ebisu_uni_gear/")

## input
activities = json2py(jsonPath = 'input/activities_20151126.json')
ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

d2s.dict2sql(
    dictionary = activities[0],
    tableName = 'moves_activities',
    database = ebisu,
    addNames = ['user'],
    addValues = ['konrad.keck@live.de'])

# print(len(activities))
# print(activities[0])
#
# print(type(ebisu))
## convert

## output

## write
