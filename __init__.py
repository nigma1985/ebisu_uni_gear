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

# ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

# def subact2sql(
#     dictionary = None, db_name = None,
#     # father_table = None, father_id = None,
#     table_name = None,
#     addNames = [], addValues = []
#     ):
#     if dictionary is None:
#         raise Exception('missing dictionary')
#     if not isinstance(dictionary, dict):
#         raise Exception('dictionary is type {}. Only dict is allowed.'.format( type(table_name) ))
#     if db_name is None:
#         raise Exception('missing database')
#     if table_name is None:
#         raise Exception('missing table name')
#     if not isinstance(table_name, str):
#         raise Exception('table name is type {}. Only string is allowed.'.format( type(table_name) ))
#     if (addNames is None):
#         raise Exception('missing list of names')
#     if (addValues is None):
#         raise Exception('missing list of values')
#     if not isinstance(addNames, (list, tuple)):
#         raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(addNames)))
#     if not isinstance(addValues, (list, tuple)):
#         raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(addValues)))
#     if len(addNames) != len(addValues):
#         raise Exception('unequal number of names ({}) and values ({})'.format(len(addNames),len(addValues)))
#
#     names = []
#     values = []
#
#     subTable = []
#
#     for d in dictionary:
#         print(d, type(dictionary[d]))
#         if isinstance(dictionary[d], (list, tuple, dict)):
#             subTable.append(d)
#         else:
#             names.append(d)
#             values.append(dictionary[d])
#
#     for i in range( len(addNames) ):
#         names.append(addNames[i])
#         values.append(addValues[i])
#
#     id = db_name.newRow(
#         table_name = table_name,
#         listNames = names,
#         listValues = values)
#
#     for sub in subTable:
#         print(sub, type(dictionary[sub]))
#         for x in dictionary[sub]:
#             print(' ', type(x), ' : ', x)

def act2sql(
    dictionary = None, db_name = None,
    # father_table = None, father_id = None,
    table_name = None,
    addNames = [], addValues = []
    ):
    if dictionary is None:
        raise Exception('missing dictionary')
    if not isinstance(dictionary, dict):
        raise Exception('dictionary is type {}. Only dict is allowed.'.format( type(table_name) ))
    if db_name is None:
        raise Exception('missing database')
    if table_name is None:
        raise Exception('missing table name')
    if not isinstance(table_name, str):
        raise Exception('table name is type {}. Only string is allowed.'.format( type(table_name) ))
    if (addNames is None):
        raise Exception('missing list of names')
    if (addValues is None):
        raise Exception('missing list of values')
    if not isinstance(addNames, (list, tuple)):
        raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(addNames)))
    if not isinstance(addValues, (list, tuple)):
        raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(addValues)))
    if len(addNames) != len(addValues):
        raise Exception('unequal number of names ({}) and values ({})'.format(len(addNames),len(addValues)))

    names = []
    values = []

    subTable = []

    for d in dictionary:
        print(d, type(dictionary[d]))
        if isinstance(dictionary[d], (list, tuple, dict)):
            subTable.append(d)
        else:
            names.append(d)
            values.append(dictionary[d])

    for i in range( len(addNames) ):
        names.append(addNames[i])
        values.append(addValues[i])

    id = db_name.newRow(
        table_name = table_name,
        listNames = names,
        listValues = values)

    for sub in subTable:
        if sub in ('summary', 'segments', 'activities'):
            print('!!', sub, type(dictionary[sub]))
            for d in dictionary[sub]:
                act2sql(
                    dictionary = d,
                    db_name = db_name,
                    table_name = table_name + '_' + sub,
                    addNames = [table_name],
                    addValues = [id])
            # subact2sql(
            #     dictionary = dictionary[sub],
            #     db_name = db_name,
            #     table_name = table_name + '_' + sub,
            #     addNames = [table_name],
            #     addValues = [id])
        else:
            print(sub, type(dictionary[sub]))
            for x in dictionary[sub]:
                print(' ', type(x), ' : ', x)

def dict2sql(
    moves_activities = None, db_name = None,
    # father_table = None, father_id = None,
    table_name = None,
    addNames = [], addValues = [],
    user = None):

    if moves_activities is None:
        raise Exception('missing json: moves_activities')
    if not isinstance(moves_activities, (list, tuple)):
        raise Exception('moves activities is type {}. Only lists or tuples allowed.'.format(type(moves_activities)))
    if db_name is None:
        raise Exception('missing database')
    if table_name is None:
        raise Exception('missing table name')
    if not isinstance(table_name, str):
        raise Exception('table name is type {}. Only string is allowed.'.format( type(table_name) ))
    if (addNames is None):
        raise Exception('missing list of names')
    if (addValues is None):
        raise Exception('missing list of values')
    if not isinstance(addNames, (list, tuple)):
        raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(addNames)))
    if not isinstance(addValues, (list, tuple)):
        raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(addValues)))
    if len(addNames) != len(addValues):
        raise Exception('unequal number of names ({}) and values ({})'.format(len(addNames),len(addValues)))
    if user is None:
        raise Exception('missing user name')
    if not isinstance(user, str):
        raise Exception('user name is type {}. Only string is allowed.'.format( type(user) ))

    addNames.append('user')
    addValues.append(user)

    for activity in moves_activities:
        act2sql(
            dictionary = activity,
            db_name = db_name,
            table_name = 'moves_activities',
            addNames = addNames,
            addValues = addValues)

dict2sql(
    moves_activities = activities,
    db_name = ebisu,
    # father_table = None, father_id = None,
    table_name = 'moves_activities',
    addNames = [],
    addValues = [],
    user = 'konrad.keck@live.de'
    )
