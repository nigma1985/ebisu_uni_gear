import urllib.request, json
from module import json2py, py2json

class tankerkoenig_api:
    # see documentation on:
    # https://creativecommons.tankerkoenig.de/

    # create variable from multiple sources
    def getVar(self,
        default = None,
        dictKey = None,
        value = None,
        theDict = {}):
        if not isinstance(theDict, dict):
            theDict = None
        elif len(theDict) < 1:
            theDict = None
        else:
            pass

        if value is not None:
            return value

        elif isinstance(dictKey, (list, tuple)) and theDict is not None:
            for entry in dictKey:
                try:
                    return theDict[entry]
                except:
                    pass
        elif isinstance(dictKey, (int, float, str)) and theDict is not None:
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
        if dictionary is None:
            raise Exception('dictionary missing!')
        elif not isinstance(dictionary, dict):
            raise Exception('dictionary is no dictionary!')
        elif len(dictionary) < 1:
            raise Exception('dictionary empty!')
        elif dictionary['provider'] not in ('tankerkoenig.de', 'Tankerkönig'):
            raise Exception('that\'s not my dictionary')
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

        self.url = 'https://creativecommons.tankerkoenig.de'
        self.format = 'json'

    def call(self,
        url = None,
        format = None,
        file = None,
        options = {}
        ):
        if url is None:
            url = self.url
        else:
            pass

        if format is None:
            format = self.format
        else:
            pass

        if options is None or len(options) < 1:
            return '{}/{}/{}'.format(url, format, file)
        elif isinstance(options, dict):
            temp = {}
            for o in options:
                if options[o] is None:
                    pass
                else:
                    temp[o] = options[o]
            return '{}/{}/{}?{}'.format(url, format, file, '&'.join([str(o) + '=' + str(temp[o]) for o in temp]))   ########


    def prt_all(self):
        print(self.lat,
            self.lng,
            self.rad,
            self.sort,
            self.type,
            self.apikey)
        print(self.dictionary)

    def get_list(self,
        lat = None,
        lng = None,
        rad = None,
        sort = None,
        type = None,
        apikey = None,
        dictionary = {}):

        norm_dict = {
            'lat' : self.getVar(
                default = self.lat,
                dictKey = 'lat',
                value = lat,
                theDict = dictionary),
            'lng' : self.getVar(
                default = self.lng,
                dictKey = 'lng',
                value = lng,
                theDict = dictionary),
            'rad' : self.getVar(
                default = self.rad,
                dictKey = 'rad',
                value = rad,
                theDict = dictionary),
            'sort' : self.getVar(
                default = self.sort,
                dictKey = 'sort',
                value = sort,
                theDict = dictionary),
            'type' : self.getVar(
                default = self.type,
                dictKey = 'type',
                value = type,
                theDict = dictionary),
            'apikey' : self.getVar(
                default = self.apikey,
                dictKey = ['apikey', 'key'],
                value = apikey,
                theDict = dictionary)
            }

        return tk.call(file = 'list.php', options = norm_dict)

    def get_prices(self,
        lat = None,
        lng = None,
        rad = None,
        sort = None,
        type = None,
        apikey = None,
        dictionary = {}):

        norm_dict = {
            'lat' : self.getVar(
                default = self.lat,
                dictKey = 'lat',
                value = lat,
                theDict = dictionary),
            'lng' : self.getVar(
                default = self.lng,
                dictKey = 'lng',
                value = lng,
                theDict = dictionary),
            'rad' : self.getVar(
                default = self.rad,
                dictKey = 'rad',
                value = rad,
                theDict = dictionary),
            'sort' : self.getVar(
                default = self.sort,
                dictKey = 'sort',
                value = sort,
                theDict = dictionary),
            'type' : self.getVar(
                default = self.type,
                dictKey = 'type',
                value = type,
                theDict = dictionary),
            'apikey' : self.getVar(
                default = self.apikey,
                dictKey = ['apikey', 'key'],
                value = apikey,
                theDict = dictionary)
            }

        return tk.call(file = 'prices.php', options = norm_dict)

    def get_detail(self,
        lat = None,
        lng = None,
        rad = None,
        sort = None,
        type = None,
        apikey = None,
        dictionary = {}):

        norm_dict = {
            'lat' : self.getVar(
                default = self.lat,
                dictKey = 'lat',
                value = lat,
                theDict = dictionary),
            'lng' : self.getVar(
                default = self.lng,
                dictKey = 'lng',
                value = lng,
                theDict = dictionary),
            'rad' : self.getVar(
                default = self.rad,
                dictKey = 'rad',
                value = rad,
                theDict = dictionary),
            'sort' : self.getVar(
                default = self.sort,
                dictKey = 'sort',
                value = sort,
                theDict = dictionary),
            'type' : self.getVar(
                default = self.type,
                dictKey = 'type',
                value = type,
                theDict = dictionary),
            'apikey' : self.getVar(
                default = self.apikey,
                dictKey = ['apikey', 'key'],
                value = apikey,
                theDict = dictionary)
            }

        return tk.call(file = 'detail.php', options = norm_dict)

    def get_complaint(self):
        pass

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
# print('options: ', opt)

# example : Heide (25746), 54.194505, 9.100905

myurl = tk.get_list(lat = 54.194505, lng = 9.100905)
print('url: ', myurl)
mytk = json2py(myurl)
print('GET: ', mytk)
