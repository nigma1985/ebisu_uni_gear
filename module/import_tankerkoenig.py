from module.connectPostgreSQL import database, dict2sql
from module import json2py, py2json
from random import sample, random

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
        calls_per_minute = 1,
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
        self.calls_per_minute = self.getVar(
            default = 1,
            dictKey = 'calls per minute',
            value = calls_per_minute,
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

    def rnd_call(self,
        calls_per_minute = None,
        apikey = None,  # apikey	Der persönliche API-Key	UUID
        dictionary = {}):
        calls_per_minute = self.getVar(
            default = self.calls_per_minute,
            dictKey = ['calls_per_minute', 'calls per minute'],
            value = calls_per_minute,
            theDict = dictionary)
        norm_dict = {
            'apikey' : self.getVar(
                default = self.apikey,
                dictKey = ['apikey', 'key'],
                value = apikey,
                theDict = dictionary)
            }

        if random() < 1 / calls_per_minute :
            pass


def tankerkoenig2sql(
    tankerkoenig_reply = None, db_name = None,
    # father_table = None, father_id = None,
    table_name = None,
    addNames = [], addValues = [],
    user = None):

    if tankerkoenig_reply is None:
        raise Exception('missing json: tankerkoenig_reply')
    if not isinstance(tankerkoenig_reply, dict):
        raise Exception('tankerkoenig_reply is type {}. Only dictionaries allowed.'.format(type(tankerkoenig_reply)))
    if db_name is None:
        raise Exception('missing database')
    if table_name is None:
        raise Exception('missing table name')
    if not isinstance(table_name, str):
        raise Exception('table name is type {}. Only string is allowed.'.format( type(table_name) ))
    if (addNames is None):
        raise Exception('missing list of names')
    if (addValues is None):
        raise Exception('missing list of values')
    if not isinstance(addNames, (list, tuple)):
        raise Exception('names are type {}. Only lists or tuples allowed.'.format(type(addNames)))
    if not isinstance(addValues, (list, tuple)):
        raise Exception('values are type {}. Only lists or tuples allowed.'.format(type(addValues)))
    if len(addNames) != len(addValues):
        raise Exception('unequal number of names ({}) and values ({})'.format(len(addNames),len(addValues)))
    if user is None:
        raise Exception('missing user name')
    if not isinstance(user, str):
        raise Exception('user name is type {}. Only string is allowed.'.format( type(user) ))

    print('--- --- --- ' + table_name + '--- --- --- ')

    addNames.append('user')
    addValues.append(user)

    # for entry in tankerkoenig_reply:
    #     print(' --','dictionary =', entry)
    #     print(' --','db_name =', db_name)
    #     print(' --','table_name =', table_name)
    #     print(' --','addNames =', addNames)
    #     print(' --','addValues =', addValues)

    dict2sql(
        dictionary = tankerkoenig_reply,
        db_name = db_name,
        table_name = table_name,
        addNames = addNames,
        addValues = addValues)
