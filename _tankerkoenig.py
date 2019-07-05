# import urllib.request, json
from module import json2py, py2json
from random import sample

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
        ids = [],
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
        self.ids = self.getVar(
            default = [],
            dictKey = 'ids',
            value = ids,
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
        # Parameter	Bedeutung	Format
        lat = None,     # lat	geographische Breite des Standortes	Floatingpoint-Zahl
        lng = None,     # lng	geographische Länge	Floatingpoint-Zahl
        rad = None,     # rad	Suchradius in km	Floatingpoint-Zahl, max: 25
        sort = None,    # sort	Sortierung	price, dist (1)
        type = None,    # type	Spritsorte	'e5', 'e10', 'diesel' oder 'all'
        apikey = None,  # apikey	Der persönliche API-Key	UUID
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
        # Parameter	Bedeutung	Format
        ids = [],       # ids	IDs der Tankstellen	UUIDs, durch Komma getrennt
        apikey = None,  # apikey	Der persönliche API-Key	UUID
        dictionary = {}):

        norm_dict = {
            'ids' : self.getVar(
                default = self.ids,
                dictKey = 'ids',
                value = ids,
                theDict = dictionary),
            'apikey' : self.getVar(
                default = self.apikey,
                dictKey = ['apikey', 'key'],
                value = apikey,
                theDict = dictionary)
            }

        if norm_dict['ids'] is None:
            return
        elif isinstance(norm_dict['ids'], (list, tuple)):
            if len(norm_dict['ids']) > 10:
                norm_dict['ids'] = sample(norm_dict['ids'], 10)
            norm_dict['ids'] = ','.join(norm_dict['ids'])
        else:
            pass

        return tk.call(file = 'prices.php', options = norm_dict)

    def get_detail(self,
        # Parameter	Bedeutung	Format
        ids = [],       # ID der Tankstelle UUID if more are given only 1 random id is processed
        apikey = None,  # apikey	Der persönliche API-Key	UUID
        dictionary = {}):

        norm_dict = {
            'id' : self.getVar(
                default = self.ids,
                dictKey = 'ids',
                value = ids,
                theDict = dictionary),
            'apikey' : self.getVar(
                default = self.apikey,
                dictKey = ['apikey', 'key'],
                value = apikey,
                theDict = dictionary)
            }

        if norm_dict['id'] is None:
            return
        elif isinstance(norm_dict['id'], (list, tuple)):
            if len(norm_dict['id']) > 1:
                norm_dict['id'] = sample(norm_dict['id'], 1)
            norm_dict['id'] = ','.join(norm_dict['id'])
        else:
            pass

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

# example : Heide (25746),
# lat/lng : 54.194505, 9.100905
# id : 3a17ce41-4292-4c29-944e-a557416c695b
# id : ee5bf10a-1c15-4fe4-9b48-12fb39758738
# id : 792fee57-1fc3-4457-9b5d-8d95626ddad4
# id : 3e25b5b1-f309-43a8-8a6d-b7baa463ff92
# id : 5f49cd98-8ccd-4978-af58-879af91f1331
# id : d5c6a7e6-ce23-4650-a8d8-00f50dc13f7e
# id : adaa7e08-4768-41ed-89c8-684f0218c997
# id : f37267d6-c8b2-480e-b9d0-1768c40fb68c
# id : d17ba98f-2cb7-4a61-830e-05bdc65ba8c7
# id : ba911f03-5026-4f38-8348-e8d76266cb24
# id : 474e5046-deaf-4f9b-9a32-9797b778f047
# id : 4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8
# id : 278130b1-e062-4a0f-80cc-19e486b4c024
mids = [
    '3a17ce41-4292-4c29-944e-a557416c695b',
    'ee5bf10a-1c15-4fe4-9b48-12fb39758738',
    '792fee57-1fc3-4457-9b5d-8d95626ddad4',
    '3e25b5b1-f309-43a8-8a6d-b7baa463ff92',
    '5f49cd98-8ccd-4978-af58-879af91f1331',
    'd5c6a7e6-ce23-4650-a8d8-00f50dc13f7e',
    'adaa7e08-4768-41ed-89c8-684f0218c997',
    'f37267d6-c8b2-480e-b9d0-1768c40fb68c',
    'd17ba98f-2cb7-4a61-830e-05bdc65ba8c7',
    'ba911f03-5026-4f38-8348-e8d76266cb24',
    '474e5046-deaf-4f9b-9a32-9797b778f047',
    '4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8',
    '278130b1-e062-4a0f-80cc-19e486b4c024']

# myurl = tk.get_list(lat = 54.194505, lng = 9.100905)
myurl = tk.get_detail(ids = mids)
print('url: ', myurl)
mytk = json2py(myurl)
print('GET: ', mytk)

for i in mytk:
    if isinstance(mytk[i], dict):
        for j in mytk[i]:
            print(i, mytk[i], mytk[i][j])
    elif isinstance(mytk[i], (tuple, list)):
        for j in mytk[i]:
            if isinstance(j, dict):
                for k in j:
                    print(i, k, j[k])
            else:
                print(i, j)
    else:
        print(i, mytk[i])
