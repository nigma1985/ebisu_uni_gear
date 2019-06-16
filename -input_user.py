import glob, os, sys, json
import module.read.pi as rpi

from pathlib import Path
from module import json2py, py2json

os.chdir("../ebisu_uni_gear/")

class frame:
    def __init__(self,
        entries = []):
        self.entries = None
        if not isinstance(entries, list) or entries is None:
            raise Exception("not list")
        elif len(entries) <= 0:
             raise Exception("missing entries")
        else:
            self.entries = entries

    def getKeys(self, data = None):
        lst = []
        if data is None:
            data = self.entries
        else:
            pass

        for line in data:
            for key in line:
                if key in lst:
                    pass
                else:
                    lst.append(key)
        print('Keys', lst)
        return lst


    def getValues(self, data = None, keys = None):
        lst = []
        if data is None:
            data = self.entries
        else:
            pass

        if keys is not None or isinstance(keys, (list, tuple)):
            pass
        else:
            keys = [keys]

        if keys is None:
            for line in data:
                for key in line:
                    if line[key] in lst:
                        pass
                    else:
                        lst.append(line[key])
        else:
            for line in data:
                for key in line:
                    if line[key] in lst:
                        pass
                    elif key in keys:
                        lst.append(line[key])

        print('Values', lst)
        return lst

    def getEntry(self, data):
        print('Entry')



class details:
    def read(self, file):
        if file is None:
            raise Exception("missing file")
        else:
            pass

        try:
            print('file {} is open'.format(file))
            return json2py(file)
        except:
            print('no file opened')
            return []
        finally:
            pass

    # Initializer / Instance Attributes
    def __init__(self,
        json = '../details.json'
        ):

        self.json = None
        if json is not None:
            self.json = json
        else:
            raise Exception("missing file")

        self.details = self.read(self.json)
        self.len = len(self.details)
        self.search = frame(entries = self.details)

    def enter(self, data = None):
        if data is None:
            data = self.details
        elif not isinstance(data, list):
            raise Exception("this is not the propper data")
        else:
            pass

        # if

    def write(self, data = None, file = None):
        if data is None:
            data = self.details
        else:
            pass

        if file is None:
            file = self.json
        else:
            pass

        print('data written to', file)
        py2json(data, file)

    def prnt_lst(self, data = None):
        if isinstance(data, (list, tuple, dict)):
            [print(n, data[n]) for n in range(len(data))]
        else:
            raise Exception("Your data is type {}. Only lists, tuples or directories allowed.".format(str(type(data))))
        # print('---------')

    def work(self, old = None):
        if old is None:
            old = self.details
            dct = self.search
        else:
            dct = frame(entries = old)

        new = {}
        theKey = None

        print("welcome to tool")
        lst = dct.getKeys()
        print(lst)
        self.prnt_lst(data = lst)
        print('x', 'add new key')
        while True:
            x = input("Enter number: ")
            if x in ('x', 'X'):
                theKey = input('please name new Key: ')
                break
            elif int(x) in range(len(lst)):
                theKey = lst[int(x)]
                print('you chose', x,'"', theKey, '"')
                break
            elif int(x) not in range(len(lst)):
                print('not in range')
            else:
                print('sorry?')

        lst = dct.getValues(keys = theKey)
        print(lst)
        self.prnt_lst(data = lst)
        print('x', 'add new value')

        while True:
            x = input("Enter number: ")
            if x in ('x', 'X'):
                new[theKey] = input('please name new Key: ')
                break
            elif int(x) in range(len(lst)):
                new[theKey] = lst[int(x)]
                print('you chose', x,'"', new[theKey], '"')
                break
            elif int(x) not in range(len(lst)):
                print('not in range')
            else:
                print('sorry?')

        print('result:  ', theKey, '/', new[theKey])
        # while True:
        #     x = input("Enter number: ")
        #     if x in ('x', 'X'):
        #         theKey = input('please name new Value: ')
        #         print('new value')
        #     elif int(x) not in range(len(lst)):
        #         print('not in range')
        #     else:
        #         theKey = lst[int(x)]
        #         print('you chose', x,'"', theKey, '"')
        #         break
        # print('done')
        input('done')

new = details()
# keys = frame(new.details)
# print(new.details, new.len)
#
# print(keys.getKeys())
# print(keys.getValues())
#
# print(keys.getValues(keys = 'user'))
# print(keys.getValues(keys = ['user', 'provider']))

new.prnt_lst(new.details)
new.work()

# new.write()

# print(
#     json2py('../details - Copy.json')
#     )
