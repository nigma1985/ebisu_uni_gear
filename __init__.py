import glob, os
# from db import database
from module import json2py
from module.connectPostgreSQL import database
from module.import_moves import move2sql

os.chdir("../ebisu_uni_gear/")

## TEST
files = glob.glob("input/*.json")

# actual run
# files = glob.glob("D:\OneDrive\Dokumente\moves_20180731\json\json\*\*.json")
# for file in glob.glob("D:\OneDrive\Dokumente\moves_20180731\json\json\*\*\*.json"):
#     files.append(file)
# for file in files:
#     print(file)

statinfo = None
## input
for f in range( len(files) ):
    statinfo = os.stat(files[f])
    files[f] = (files[f], statinfo.st_size)

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list

# sort list with key
files.sort(key=takeSecond)

# print list
for file in files:
    print(file)

size = 0
file = 0
# type = ''
# path = None

ebisu = database(db_type=None, host='copyright', user='pi', password='21255Dohren', dbname='test')

scope = []
for f in files:
    scope.append(f[1])

if sum(scope) < 4096:
    scope = sum(scope)
else:
    #scope = 10000000
    scope = 4096

while (size < scope) and (file < len(files)):
    path = files[file][0]
    moves = json2py(jsonPath = path)

    if 'summary' in path:
        type = 'summary'
    if 'storyline' in path:
        type = 'storyline'
    if 'places' in path:
        type = 'places'
    if 'activities'in path:
        type = 'activities'

    move2sql(
        moves_activities = moves,
        db_name = ebisu,
        # father_table = None, father_id = None,
        table_name = 'moves',
        addNames = [type],
        addValues = [True],
        user = 'konrad.keck@live.de'
        )

    size = size + files[file][1]
    file = file + 1
    print('>> ', round(size/scope*100,ndigits=2), '%  ', file, 'files  ', type, ' | ', path)
