# import urllib.request, json
from module import json2py, py2json
from random import sample, random
from module.import_tankerkoenig import tankerkoenig_api




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


# url = "https://creativecommons.tankerkoenig.de/json/list.php?lat={}&lng={}&rad={}&sort={}&type={}&apikey={}".format(lat, lng, rad, sort, type, apikey)
#
# with urllib.request.urlopen(url) as site:
#     data = json.loads(site.read().decode())
#     print(data)


tk = tankerkoenig_api(rad = 2.5, dictionary = call)
tk.prt_all()
# print('options: ', opt)

# example : Heide (25746),
# lat/lng : 54.194505, 9.100905
# id : 3a17ce41-4292-4c29-944e-a557416c695b
# id : ee5bf10a-1c15-4fe4-9b48-12fb39758738
# id : 792fee57-1fc3-4457-9b5d-8d95626ddad4
# id : 3e25b5b1-f309-43a8-8a6d-b7baa463ff92
# id : 5f49cd98-8ccd-4978-af58-879af91f1331
# id : d5c6a7e6-ce23-4650-a8d8-00f50dc13f7e
# id : adaa7e08-4768-41ed-89c8-684f0218c997
# id : f37267d6-c8b2-480e-b9d0-1768c40fb68c
# id : d17ba98f-2cb7-4a61-830e-05bdc65ba8c7
# id : ba911f03-5026-4f38-8348-e8d76266cb24
# id : 474e5046-deaf-4f9b-9a32-9797b778f047
# id : 4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8
# id : 278130b1-e062-4a0f-80cc-19e486b4c024
mids = [
    '3a17ce41-4292-4c29-944e-a557416c695b',
    'ee5bf10a-1c15-4fe4-9b48-12fb39758738',
    '792fee57-1fc3-4457-9b5d-8d95626ddad4',
    '3e25b5b1-f309-43a8-8a6d-b7baa463ff92',
    '5f49cd98-8ccd-4978-af58-879af91f1331',
    'd5c6a7e6-ce23-4650-a8d8-00f50dc13f7e',
    'adaa7e08-4768-41ed-89c8-684f0218c997',
    'f37267d6-c8b2-480e-b9d0-1768c40fb68c',
    'd17ba98f-2cb7-4a61-830e-05bdc65ba8c7',
    'ba911f03-5026-4f38-8348-e8d76266cb24',
    '474e5046-deaf-4f9b-9a32-9797b778f047',
    '4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8',
    '278130b1-e062-4a0f-80cc-19e486b4c024']

# myurl = tk.get_list(lat = 54.194505, lng = 9.100905)
# myurl = tk.get_prices(ids = mids)
# myurl = tk.get_detail(ids = mids)
# print('url: ', myurl)
# mytk = json2py(myurl)
# print('GET: ', mytk)
#
# for i in mytk:
#     if isinstance(mytk[i], dict):
#         for j in mytk[i]:
#             print(i, mytk[i], mytk[i][j])
#     elif isinstance(mytk[i], (tuple, list)):
#         for j in mytk[i]:
#             if isinstance(j, dict):
#                 for k in j:
#                     print(i, k, j[k])
#             else:
#                 print(i, j)
#     else:
#         print(i, mytk[i])

# print(tk.get_list(lat = 54.194505, lng = 9.100905))
# print(tk.get_prices(ids = mids))
# print(tk.get_detail(ids = mids))'

# lst = json2py('../list.json')
# prcs = json2py('../prices.json')
# dtls = json2py('../detail.json')
lst = tk.get_list(lat = -54.194505, lng = -9.100905)
# prcs = tk.get_prices(ids = mids)
# dtls = tk.get_detail(ids = mids)

print('list.php', lst)
# print('prices.php', prcs)
# print('detail.php', dtls)
