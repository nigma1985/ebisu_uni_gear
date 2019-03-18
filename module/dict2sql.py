# import module.list2sql as l2s

def dict2sql(dictionary = None, tableName = None, database = None, addNames = [], addValues = []):

    print(type(dictionary), " : ", dictionary)
    print(tableName)
    print(database)
    print(addNames)
    print(addValues)

    if dictionary is None:
        raise Exception('missing dictionary')
    if database is None:
        raise Exception('missing database')
    if tableName is None:
        raise Exception('missing table name')
    if not isinstance(dictionary, dict):
        raise Exception('dictionary is no dictionary')
    if len(dictionary) == 0:
        return('no items in dictionary')
    if not isinstance(addNames, (list, tuple)):
        raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(addNames)))
    if not isinstance(addValues, (list, tuple)):
        raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(addNames)))
    if len(addNames) != len(addValues):
        raise Exception('unequal number of additional names ({}) and values ({})'.format(len(addNames),len(addValues)))

    newList = []
    newTuple = []
    newDict = []

    for add in range(len(addNames)):
        dictionary[addNames[add]] = addValues[add]

    for entry in dictionary:
        print(' {} : {} ({})'.format(entry, dictionary[entry], type(dictionary[entry])))
