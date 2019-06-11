import glob, os, sys, json
import module.read.pi as rpi

from pathlib import Path
from module import json2py, py2json

os.chdir("../ebisu_uni_gear/")


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

    def write(self, data, file):
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
