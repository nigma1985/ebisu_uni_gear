from module.connectPostgreSQL import database

def dict2sql(
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

    print('--' + table_name + '--')
    names = []
    values = []

    subTable = []

    for d in dictionary:
        # print(d, type(dictionary[d]))
        if isinstance(dictionary[d], (list, tuple)):
            subTable.append(d)
        elif isinstance(dictionary[d], (dict)):
            if d == 'id':
                names.append(table_name + '_' + d)
            else:
                names.append(d)
            values.append(
                dict2sql(
                    dictionary = dictionary[d],
                    db_name = db_name,
                    table_name = d)
            )
        else:
            if d == 'id':
                names.append(table_name + '_' + d)
            else:
                names.append(d)
            values.append(dictionary[d])

    for i in range( len(addNames) ):
        if addNames[i] == 'id':
            names.append(table_name + '_' + addNames[i])
        else:
            names.append(addNames[i])
        values.append(addValues[i])

    id = db_name.newRow(
        table_name = table_name,
        listNames = names,
        listValues = values)

    for sub in subTable:
        if sub in ('summary', 'segments', 'activities', 'place', 'trackPoints'):
            # print('!!', sub, type(dictionary[sub]))
            for d in dictionary[sub]:
                dict2sql(
                    dictionary = d,
                    db_name = db_name,
                    table_name = sub,
                    addNames = [table_name],
                    addValues = [id])
        else:
            # print(sub, type(dictionary[sub]))
            for x in dictionary[sub]:
                print(' ', type(x), ' : ', x)

    return id

def mact2sql(
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

    print('--- --- --- ' + table_name + '--- --- --- ')

    addNames.append('user')
    addValues.append(user)

    for entry in moves_activities:
        dict2sql(
            dictionary = entry,
            db_name = db_name,
            table_name = table_name,
            addNames = addNames,
            addValues = addValues)
