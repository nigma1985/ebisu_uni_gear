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

            ## for right join (n:1)
            if d == 'id':
                names.append(table_name + '_' + d)
            else:
                names.append(d)
                # print(' -1', 'dictionary =', dictionary[d])
                # print(' -1', 'db_name =', db_name)
                # print(' -1', 'table_name =', d)
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

    ## regular entry / new row
    # print(' -2', 'table_name =', table_name)
    # print(' -2', 'listNames =', names)
    # print(' -2', 'listValues =', values)
    id = db_name.newRow(
        table_name = table_name,
        listNames = names,
        listValues = values)


    ## for left join (1:n)
    for sub in subTable:
        for d in dictionary[sub]:
            dict2sql(
                dictionary = d,
                db_name = db_name,
                table_name = sub,
                addNames = [table_name],
                addValues = [id])

    return id

def move2sql(
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
        # print(' --','dictionary =', entry)
        # print(' --','db_name =', db_name)
        # print(' --','table_name =', table_name)
        # print(' --','addNames =', addNames)
        # print(' --','addValues =', addValues)

        dict2sql(
            dictionary = entry,
            db_name = db_name,
            table_name = table_name,
            addNames = addNames,
            addValues = addValues)
