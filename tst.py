# import glob, os
# # from db import database
# from module import json2py
# from module.connectPostgreSQL import database
# from module.import_moves import mact2sql
#
# ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')
# ebisu.newRow(table_name = 'myTest', listNames = ['driver', 'UsER'], listValues = ['Dummy', 'Konrad'])

def chkBalance(a, b):
    ## check two lists for substance and symetry
    if (a is None) or (len(a) == 0) or (b is None) or (len(a) == 0):
        return 'missing value'
    if not isinstance(a, (list, tuple)) or not isinstance(b, (list, tuple)):
        return 'missing list (types : {}/{})'.format(type(a),type(b))
    if len(a) != len(b):
        return 'uneven lists (lengths : {}/{})'.format(len(a),len(b))
    else:
        return False

bal = chkBalance('[1,2]',[1,2,3])

if bal:
    print('error', bal)
else:
    print('all right', bal)

#print('my text ', bal)
