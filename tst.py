import json
from module import json2py, py2json

file = 'data.json'
data = {}


try:
    data = json2py(file)
except:
    data['name'] = 'JohnDoe'
    data['place'] = 'AnotherTown'
    data['time'] = 'later'
    data['var'] = 0
    data['nothing'] = None


data['var'] = data['var'] + 1


py2json(data, file)
