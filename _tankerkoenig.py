import urllib.request, json
from module import json2py, py2json

class tankerkoenig_api:
    def getVar(self,
        default = None,
        dictKey = None,
        value = None,
        theDict = {}):
        if any(
            theDict is None,
            not isinstance(dictKey, dict),
            len(dictKey) < 1):
            raise Exception("dict missing")
        elif value is not None:
            return value
        elif isinstance(dictKey, (list, tuple)):
            for entry in dictKey:
                try:
                    return theDict[entry]
                except:
                    pass
        elif isinstance(dictKey, (number, str)):
            try:
                return theDict[dictKey]
            except:
                pass
        else:
            return default

    def __init__(self,
        dictionary = {},
        lat = None,
        lng = None,
        rad = None,
        sort = 'dist',
        type = 'all',
        apikey = None
        ):
        self.dictionary = None
        if any(
            len(dictionary) < 1,
            dictionary['provider'] not in ('tankerkoenig.de', 'Tankerkönig'),
            not isinstance(dictionary, dict),
            dictionary is None
        ):
            raise Exception('dictionary missing!')
        else:
            self.dictionary = dictionary

        self.lat = self.getVar(
            default = None,
            dictKey = 'lat',
            value = lat,
            theDict = self.dictionary)
        self.lng = self.getVar(
            default = None,
            dictKey = 'lng',
            value = lng,
            theDict = self.dictionary)
        self.rad = self.getVar(
            default = 5.0,
            dictKey = 'rad',
            value = rad,
            theDict = self.dictionary)
        self.sort = self.getVar(
            default = 'dist',
            dictKey = 'sort',
            value = sort,
            theDict = self.dictionary)
        self.type = self.getVar(
            default = 'all',
            dictKey = 'type',
            value = type,
            theDict = self.dictionary)
        self.apikey = self.getVar(
            default = None,
            dictKey = ['apikey', 'key'],
            value = apikey,
            theDict = self.dictionary)

    def prt_all(self):
        print(self.lat,
            self.lng,
            self.rad,
            self.sort,
            self.type,
            self.apikey)
        print(self.dictionary)

details = '../details.json'
details = json2py(details)

print('details', details)
tankerkoenig = []
for d in details:
    if d['provider'] == 'tankerkoenig.de':
        tankerkoenig.append(d)
    else:
        pass

print('tankerkoenig', tankerkoenig)
call = tankerkoenig[0]

print(call['key'])

# lat = 33.993815
# lng = 10.540907
# rad = 1.5
# sort = 'dist'
# type = all
apikey = call['key']


# url = "https://creativecommons.tankerkoenig.de/json/list.php?lat={}&lng={}&rad={}&sort={}&type={}&apikey={}".format(lat, lng, rad, sort, type, apikey)
#
# with urllib.request.urlopen(url) as site:
#     data = json.loads(site.read().decode())
#     print(data)


tk = tankerkoenig_api(rad = 2.5, dictionary = call)
tk.prt_all()
