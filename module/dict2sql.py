from list2sql import list2sql

def dict2sql(dictionary = None, tableName = None, database = None, addNames = [], addValues = []):
    if dictionary is None:
        raise Exception('missing dictionary')
    if database is None:
        raise Exception('missing database')
    if tableName is None:
        raise Exception('missing table name')
    if isinstance(dictionary, dict):
        raise Exception('dictionary is no dictionary')
    if len(dictionary) == 0:
        return('no items in dictionary')
    if len(addNames) != len(addValues):
        raise Exception('unequal number of additional names ({}) and values ({})'.format(len(addNames),len(addValues)))

    newList = []
    newTuple = []
    newDict = []

    for add in len(addNames):
        dictionary[addNames[add]] = addValues[add]
