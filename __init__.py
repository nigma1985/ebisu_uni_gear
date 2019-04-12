import glob, os
# import module.read.pi as rpi
# from db import database
from module import json2py, removeFile
from module.connectPostgreSQL import database
from module.import_moves import move2sql

os.chdir("../ebisu_uni_gear/")

# cpu_use = rpi.cpu_percent()
# ram = rpi.virtual_memory()


## TEST
files = glob.glob("input/*.json")
# files = glob.glob("../json/*.json")

# actual run
# files = glob.glob("/home/pi/json/moves/*.json")
# files.extend(glob.glob("/home/pi/json/moves/*/*.json"))
# files.extend(glob.glob("/home/pi/json/moves/*/*/*.json"))

# for file in glob.glob("../json/moves/*/*/*.json"):
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

if sum(scope) < (2 ** 12):
    scope = sum(scope)
else:
    scope = (2 ** 12)

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

    # print('->>','moves_activities =', moves)
    # # print('db_name =', ebisu)
    # print('table_name =', 'moves')
    # print('addNames =', [type])
    # print('addValues =', [True])
    # print('user =', 'konrad.keck@live.de')

    move2sql(
        moves_activities = moves,
        db_name = ebisu,
        table_name = 'moves',
        addNames = [type],
        addValues = [True],
        user = 'konrad.keck@live.de'
        )

    # # removeFile(path)
    size = size + files[file][1]
    file = file + 1
    print('>> ', round(size/scope*100,ndigits=2), '%  ', file, 'files  ', type, ' | ', path)
