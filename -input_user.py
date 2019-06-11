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

    def getHeads(self, data):
        print('heads')
    def getLines(self, data):
        print('lines')
    def getEntries(self, data):
        print('entries')



class details:
    def read(self, file):
        if file is None:
            raise Exception("missing file")
        else:
            pass

        try:
            print('file {} opened'.format(file))
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

        if

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
print(new.details, new.len)
new.write()
