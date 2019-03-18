import module.dict2sql as d2s

def list2sql(listing = None, tableName = None, database = None, addItem = []):
    if listing is None:
        raise Exception('missing list')
    if database is None:
        raise Exception('missing database')
    if tableName is None:
        raise Exception('missing table name')
    if isinstance(listing, list):
        raise Exception('dictionary is no list')
    if len(listing) == 0:
        return('no items in list')

    newList = []
    newTuple = []
    newDict = []

    for add in len(addNames):
        dictionary[addNames[add]] = addValues[add]
