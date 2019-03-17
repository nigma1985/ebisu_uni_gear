import os
import json

def dict2sql(dictionary = None, tableName = None, database = None, addNames = [], addValues = []):
    if dictionary is None:
        raise Exception('missing dictionary')
    if database is None:
        raise Exception('missing database')
    if tableName is None:
        raise Exception('missing table name')
    if isinstance(dictionary, dict):
        raise Exception('dictionary is no dictionary')
    if len(dictionary) == 0:
        return('no items in dictionary')
    if len(addNames) != len(addValues):
        raise Exception('unequal number of additional names ({})/values ({})'.format(len(addNames),len(addValues)))

    newList = []
    newTuple = []
    newDict = []

    for add in len(addNames):
        dictionary[addNames[add]] = addValues[add]

#
# dict2sql(addNames = ['ich', 'du', 'er'], addValues = [1,2,3,4])
#
#
# os.chdir("../ebisu_uni_gear/")
#
# print(os.getcwd())
#
# with open('input/activities_20151126.json', 'r') as f:
#     jsonActivities = json.load(f)
#
# newList = []
# newTuple = []
# newDict = []
#
# for day in jsonActivities:
#     for entry in day:
#         if isinstance(day[entry], dict):
#             print('dict')
#             newDict.append(entry)
#         if isinstance(day[entry], tuple):
#             print('tuple')
#             newTuple.append(entry)
#         if isinstance(day[entry], list):
#             print('list')
#             newList.append(entry)
#         else:
#             # apply data and get ID
#             print(entry, ': ', day[entry])
#
#     if len(newList) > 0:
#         print('lists: '+ str(len(newList)))
#         # for item in newList:
#             # create list-Table
#
#     if len(newTuple) > 0:
#         print('tuples: '+ str(len(newTuple)))
#         # for item in newList:
#             # create tuple-Table
#
#     if len(newDict) > 0:
#         print('dicts: '+ str(len(newDict)))
#         # for item in newList:
#             # create dict-Table
#
#
#
#
# ## PSEUDO CODE ##
# # moves saves as lists.
# # Each day is one entry.
# # Each entry is a dict.
# # Each dict consists of summery of day and sequences as well as daily data.
# # Summery and Sequence are dicts. Each may contain more substructures (list, dict, tuple, ...)
# #
# # For singular items (i.e. one date, one int, one number, one name, ...) in a dict a table / two-dimensional metrix should be created.
# # For each substructure a new table should be created with a link to the overlaying structure.
# #
# #
# # for each item in list:
# #
# #
# #     hand over IDs and table-name
# #     test if dict:
# #         if dict, use item-name and item :
# #             create SQL Statement to check if line already exists
# #                 ==> if yes: get ID / update changes
# #                 ==> if no : create line and get ID
# #         if tuple, use ...
# #             create SQL Statement to check if line already exists
# #                 ==> if yes: get ID / update changes
# #                 ==> if no : create line and get ID
# #         if list, use overlaying ID and name :
# #             create SQL Statement to check if line already exists
# #                 ==> if yes: get ID / update changes
# #                 ==> if no : create line and get ID
