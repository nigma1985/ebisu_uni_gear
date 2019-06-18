import urllib.request, json
from module import json2py, py2json

details = '../details.json'
details = json2py(details)

print('details', details)
tankerkoenig = []
for d in details:
    if d['provider'] == 'tankerkoenig.de':
        tankerkoenig.append(d)
    else:
        pass

print('tankerkoenig', tankerkoenig)
call = tankerkoenig[0]

print(call['key'])

# lat = 33.993815
# lng = 10.540907
# rad = 1.5
# sort = 'dist'
# type = all
apikey = call['key']
#
# url = "https://creativecommons.tankerkoenig.de/json/list.php?lat={}&lng={}&rad={}&sort={}&type={}&apikey={}".format(lat, lng, rad, sort, type, apikey)
#
# with urllib.request.urlopen(url) as site:
#     data = json.loads(site.read().decode())
#     print(data)
