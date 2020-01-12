import glob, os, openpyxl
from module import json2py, py2json
import numpy as np
import pandas as pd

base_path = "C:\\Users\\Konrad\\OneDrive\\Dokumente\\kto"
sep = os.path.sep
ext = "20200111"

print(sep)


files = (
    "539947056",
    "2204012900",
    "2204012920",
    "2204012950",
    "2204012955")

jsn = []
keys = set()

for file in files:
    result = json2py("{}{}{}-{}.json".format(base_path, sep, file, ext))
    # print(type(result), result)
    for item in result:
        item['ACCOUNT'] = file
        jsn.append(item)
        for key in item:
            keys.add(key)

# for x in jsn:
#     print(x)

print(keys)

frm = pd.DataFrame(jsn)
frm.to_excel("{}{}{}-{}.xlsx".format(base_path, sep, "output", ext))
# print(frm)
