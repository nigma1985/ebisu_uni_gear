import os
# from db import database
from module import json2py
from module.connectPostgreSQL import database
from module.import_moves import mact2sql

os.chdir("../ebisu_uni_gear/")

## input
# activities = json2py(jsonPath = 'input/activities_20151126.json')
# activities = json2py(jsonPath = 'D:/OneDrive/Dokumente/moves_20180731/json/json/full/activities.json')
# places = json2py(jsonPath = 'D:/OneDrive/Dokumente/moves_20180731/json/json/full/places.json')
# storyline = json2py(jsonPath = 'D:/OneDrive/Dokumente/moves_20180731/json/json/full/storyline.json')
# summary = json2py(jsonPath = 'D:/OneDrive/Dokumente/moves_20180731/json/json/full/summary.json')

ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

# ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

 
# mact2sql(
#     moves_activities = summary,
#     db_name = ebisu,
#     # father_table = None, father_id = None,
#     table_name = 'moves',
#     addNames = ['export'],
#     addValues = ['summary'],
#     user = 'konrad.keck@live.de'
#     )
