a = {'ID' : 1, 'Name' : 'Albert'}
b = {'ID' : 2, 'Name' : 'Berta'}
c = {'ID' : 3, 'Name' : 'Chile'}
d = {'ID' : 4, 'Name' : 'Dummy'}

dict = [a, b, c, d]

for item in dict:
    print(item)
    item["user"] = 'Konrad'
    for i in item:
        print(i, ' : ', item[i])

import module.dict2sql
