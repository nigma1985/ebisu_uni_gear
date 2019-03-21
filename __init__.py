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

# d2s.dict2sql(
#     dictionary = activities[0],
#     tableName = 'moves_activities',
#     database = ebisu,
#     addNames = ['user'],
#     addValues = ['konrad.keck@live.de'])
# x = ebisu.results

ebisu.setSQL('''
    CREATE TABLE IF NOT EXISTS {} (
        "id" SERIAL PRIMARY KEY,
        {} JSON,
        {} TEXT
    );'''.format(
        '"json_test"',
        '"activities"',
        '"user"'))

ebisu.setSQL('''
    ALTER TABLE IF EXISTS {}
    ADD COLUMN IF NOT EXISTS {} TEXT
    ;'''.format(
        '"json_test"',
        '"user"'))
        
ebisu.setSQL('''
    ALTER TABLE IF EXISTS {}
    ADD COLUMN IF NOT EXISTS {} TEXT,
    ADD COLUMN IF NOT EXISTS {} TEXT,
    ADD COLUMN IF NOT EXISTS {} TEXT
    ;'''.format(
        '"json_test"',
        '"user"',
        '"driver"',
        '"date"'))

ebisu.setSQL('''
    INSERT INTO "json_test" (
        "id",
        "activities",
        "user",
        "driver",
        "date")
    VALUES (
        DEFAULT,
        DEFAULT,
        'bsp1',
        'ich',
        DEFAULT)
    ;''')
#
# ebisu.setSQL('''
#     INSERT INTO {} (
#         {},
#         {})
#     VALUES (
#         {},
#         {}
#     );'''.format(
#         '"json_test"',
#         '"activities"',
#         '"driver"',
#         '"bsp2"',
#         '"du"'))
#
# ebisu.setSQL('''
#     INSERT INTO {} (
#         {},
#         {},
#         {})
#     VALUES (
#         {},
#         {},
#         {}
#     );'''.format(
#         '"json_test"',
#         '"activities"',
#         '"user"',
#         '"driver"',
#         '"bsp3"',
#         '"er"',
#         '"sie"'))
#
# ebisu.setSQL('''
#     INSERT INTO {} (
#         {},
#         {})
#     VALUES (
#         {},
#         {})
#     ON CONFLICT (
#         {},
#         {}
#     ) DO NOTHING;'''.format(
#         '"json_test"',
#         '"activities"',
#         '"user"',
#         '"bsp1"',
#         '"ich"',
#         '"activities"',
#         '"user"'))


# ebisu.setSQL('''
#     INSERT INTO {}(
#         {},
#         {})
#     VALUES (
#         {},
#         {})
#     ;'''.format('"json_test"',
#         '"activities"',
#         '"user"',
#         activities,
#         'user'))

#
# for entry in activities:
#     ebisu.setSQL('''
#         INSERT INTO {}(
#             {},
#             {})
#         VALUES (
#             {},
#             {})
#         ;'''.format('"json_test"',
#             '"activities"',
#             '"user"',
#             entry,
#             'user'))


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
