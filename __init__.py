import os
# from db import database
from module import json2py
from module.connectPostgreSQL import database
import module.dict2sql as d2s
import module.list2sql as l2s

os.chdir("../ebisu_uni_gear/")

## input
# activities = json2py(jsonPath = 'input/activities_20151126.json')
activities = json2py(jsonPath = 'input/activities_20180101.json')
ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

# d2s.dict2sql(
#     dictionary = activities[0],
#     tableName = 'moves_activities',
#     database = ebisu,
#     addNames = ['user'],
#     addValues = ['konrad.keck@live.de'])
# x = ebisu.results
# ebisu.json2sql(json = activities)
# ebisu.createTable(table_name = 'test', listNames = ['Stadt', 'Land', 'Fluss'])
# ebisu.newRow(table_name = 'test', listNames = ['Stadt', 'Land', 'Fluss'], listValues = ['Aachen', 'Brandenburg', 'Chile'])





# for result in ebisu.results:
#     print(result)

# print(len(activities))
# print(activities[0])
#
# print(type(ebisu))
## convert

## output

## write
