import os
import json

os.chdir("D:/OneDrive/Dokumente/moves_20180731/json")

print(os.getcwd())


## jsonStoryline = open("json/full/storyline.json")
with open('json/full/activities.json', 'r') as f:
    jsonActivities = json.load(f)
print(len(jsonActivities))
print(jsonActivities[1])


# ## jsonSummary = open("json/full/summary.json")
# with open('json/full/places.json', 'r') as f:
#     jsonPlaces = json.load(f)
# print(len(jsonPlaces))
# print(jsonPlaces[1])


# ## jsonPlaces = open("json/full/places.json")
# with open('json/full/storyline.json', 'r') as f:
#     jsonStoryline = json.load(f)
# print(len(jsonStoryline))
# print(jsonStoryline[1])


## jsonActivities =open("json/full/activities.json")
# with open('json/full/summary.json', 'r') as f:
#     jsonSummary = json.load(f)
# print(len(jsonSummary))
# print(jsonSummary[1])

lineOne = jsonActivities[6]
print(lineOne['date'])
print(lineOne['summary'])
print(len(lineOne['summary']))
print(lineOne['segments'])
print(len(lineOne['segments']))
print(lineOne['caloriesIdle'])
#print(len(lineOne['caloriesIdle']))
print(lineOne['lastUpdate'])
#print(len(lineOne['lastUpdate']))

lineOneSummary = lineOne['summary']
print(len(lineOneSummary))

lineOneSegments = lineOne['segments']
print(len(lineOneSegments))

for seg in lineOneSegments:
    print(seg)
