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

new = details()
keys = frame(new.details)
print(new.details, new.len)

print(keys.getKeys())
print(keys.getValues())

print(keys.getValues(keys = 'user'))
print(keys.getValues(keys = ['user', 'provider']))


new.write()

# print(
#     json2py('../details - Copy.json')
#     )
