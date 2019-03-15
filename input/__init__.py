import os
import json

os.chdir("../ebisu_uni_gear/")

print(os.getcwd())

with open('input/activities_20151126.json', 'r') as f:
    jsonActivities = json.load(f)
print(len(jsonActivities))
print(jsonActivities[0])
#
# for item in jsonActivities[0]:
#     print(item + " : " + str(jsonActivities[0][item]))
#
# print(jsonActivities[0]['segments'])
#
# print()
# for item in jsonActivities[0]['segments']:
#     print(str(jsonActivities[0][item]))



print('------')

print(type(jsonActivities))
for day in jsonActivities:
    print(type(day))
    if isinstance(day, (list,tuple,dict)):
        for item in day:
            if isinstance(item, (list,tuple,dict)):
                for i in item:
                    print('  ', item, ' : ', i)
            else:
                print(' ', day, ' : ', item)
    else:
        print(day)
#
# lineOne = jsonActivities[6]
# print(lineOne['date'])
# print(lineOne['summary'])
# print(len(lineOne['summary']))
# print(lineOne['segments'])
# print(len(lineOne['segments']))
# print(lineOne['caloriesIdle'])
# #print(len(lineOne['caloriesIdle']))
# print(lineOne['lastUpdate'])
# #print(len(lineOne['lastUpdate']))
#
# lineOneSummary = lineOne['summary']
# print(len(lineOneSummary))
#
# lineOneSegments = lineOne['segments']
# print(len(lineOneSegments))
#
# for seg in lineOneSegments:
#     print(seg)
