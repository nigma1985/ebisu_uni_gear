import glob, os, sys, json
import module.read.pi as rpi

from pathlib import Path
from module import json2py, py2json

os.chdir("../ebisu_uni_gear/")



data = []
resume = file.replace(".zip", ".json").replace(".ZIP", ".json")
try:
    data = json2py(resume)
except:
    data['password number'] = p
    data['password'] = None
    data['file'] = file

class unzip:
    def getDir(self, path):
        if path is None:
            return
        return Path(path).parent.absolute()

    # Initializer / Instance Attributes
    def __init__(self,
        zipfile = None,
        start = time.mktime(datetime.now().timetuple()),
        password = None,
        passnum = None,
        passnum0 = 0):

        self.zipfile = None
        if zipfile is not None:
            self.zipfile = zipfile
        else:
            raise
