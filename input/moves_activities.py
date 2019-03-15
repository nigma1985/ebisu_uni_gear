import os
import json

os.chdir("../ebisu_uni_gear/")

print(os.getcwd())

with open('input/activities_20151126.json', 'r') as f:
    jsonActivities = json.load(f)

newList = []
newTuple = []
newDict = []

for day in jsonActivities:
    if isinstance(day, dict):
        newDict.append(day)
    if isinstance(day, tuple):
        newTuple.append(day)
    if isinstance(day, list):
        newList.append(day)
    else:
        # apply data and get ID

    if len(newList) > 0:
        for item in newList:
            # create list-Table

    if len(newTuple) > 0:
        for item in newList:
            # create tuple-Table

    if len(newDict) > 0:
        for item in newList:
            # create dict-Table




## PSEUDO CODE ##
# moves saves as lists.
# Each day is one entry.
# Each entry is a dict.
# Each dict consists of summery of day and sequences as well as daily data.
# Summery and Sequence are dicts. Each may contain more substructures (list, dict, tuple, ...)
#
# For singular items (i.e. one date, one int, one number, one name, ...) in a dict a table / two-dimensional metrix should be created.
# For each substructure a new table should be created with a link to the overlaying structure.
#
#
# for each item in list:
#
#
#     hand over IDs and table-name
#     test if dict:
#         if dict, use item-name and item :
#             create SQL Statement to check if line already exists
#                 ==> if yes: get ID / update changes
#                 ==> if no : create line and get ID
#         if tuple, use ...
#             create SQL Statement to check if line already exists
#                 ==> if yes: get ID / update changes
#                 ==> if no : create line and get ID
#         if list, use overlaying ID and name :
#             create SQL Statement to check if line already exists
#                 ==> if yes: get ID / update changes
#                 ==> if no : create line and get ID
