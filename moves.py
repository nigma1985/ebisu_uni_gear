import glob, os, sys
import module.read.pi as rpi
# from db import database
from module import json2py, removeFile
from module.connectPostgreSQL import database
from module.import_moves import move2sql

# os.chdir("../ebisu_uni_gear/")

ram = rpi.virtual_memory()


## TEST
# files = glob.glob("input/*.json")
# files = glob.glob("../json/*.json")
cpu = rpi.cpu_percent()
ram = rpi.virtual_memory()
ram = ram.percent

if (cpu > (2/3*100)) or (ram > (4/5*100)):
    print(datetime.now())
    print("> CPU: {}%".format(cpu))
    print("> RAM: {}%".format(ram))
    sys.exit()

# actual run
files = glob.glob("/home/pi/json/moves/*.json")
files.extend(glob.glob("/home/pi/json/moves/*/*.json"))
files.extend(glob.glob("/home/pi/json/moves/*/*/*.json"))

# for file in glob.glob("../json/moves/*/*/*.json"):
#     files.append(file)
# for file in files:
#     print(file)

if len(files) == 0 or files is None:
    sys.exit()

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

if sum(scope) < (2 ** 15):
    scope = sum(scope)
else:
    scope = (2 ** 15)

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

    removeFile(path)
    size = size + files[file][1]
    file = file + 1
    print('>> ', round(size/scope*100,ndigits=2), '%  ', file, 'files  ', type, ' | ', path)
