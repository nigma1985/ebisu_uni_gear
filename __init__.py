import os
# from db import database
from module import json2py
from module.connectPostgreSQL import database
from module.import_moves import mact2sql

os.chdir("../ebisu_uni_gear/")

## input
# activities = json2py(jsonPath = 'input/activities_20151126.json')
activities = json2py(jsonPath = 'input/activities_20180108.json')
places = json2py(jsonPath = 'input/places_20180115.json')
storyline = json2py(jsonPath = 'input/storyline_20180122.json')
summary = json2py(jsonPath = 'input/summary_20180205.json')

ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

# ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

mact2sql(
    moves_activities = summary,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_summary',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
mact2sql(
    moves_activities = places,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_places',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
mact2sql(
    moves_activities = activities,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_activities',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
mact2sql(
    moves_activities = storyline,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_storyline',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )


activities = json2py(jsonPath = 'input/activities_20180101.json')
places = json2py(jsonPath = 'input/places_20180101.json')
storyline = json2py(jsonPath = 'input/storyline_20180101.json')
summary = json2py(jsonPath = 'input/summary_20180101.json')

mact2sql(
    moves_activities = summary,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_summary',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
mact2sql(
    moves_activities = places,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_places',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
mact2sql(
    moves_activities = activities,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_activities',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
mact2sql(
    moves_activities = storyline,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_storyline',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
