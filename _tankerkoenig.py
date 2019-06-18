import urllib.request, json
from module import json2py, py2json

class tankerkoenig:
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


        self.lat = None  ## default value
        if lat is not None:
            self.lat = lat
        else:
            try:
                self.lat = self.dictionary['lat']
            exception:
                pass

        self.lng = None  ## default value
        if lng is not None:
            self.lng = lng
        else:
            try:
                self.lng = self.dictionary['lng']
            exception:
                pass

        self.rad = None
        if lng is not None:
            self.rad = rad
        else:
            try:
                self.rad = self.dictionary['rad']
            exception:
                self.rad = 5.0 ## default value

        self.sort = None
        if sort is not None:
            self.sort = sort
        else:
            try:
                self.sort = self.dictionary['sort']
            exception:
                self.sort = 'dist' ## default value

        self.type = None
        if type is not None:
            self.type = type
        else:
            try:
                self.type = self.dictionary['type']
            exception:
                self.type = 'all' ## default value


        self.type = None
        if type is not None:
            self.type = type
        else:
            try:
                self.type = self.dictionary['type']
            exception:
                self.type = 'all'  ## default value

        self.apikey = None ## default value
        if apikey is not None:
            self.apikey = apikey
        else:
            try:
                self.apikey = self.dictionary['apikey']
            exception:
                try:
                    self.apikey = self.dictionary['key']
                exception:
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
