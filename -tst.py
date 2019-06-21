# tst_list = [None, 1, 2, 3, None, 'A', 'B', 'C', None]
# print(tst_list)
#
# [print(t if t is not None) for t in tst_list]

x = {'a': 'alpha', 'b': 'bertha', 'c': 'chrlie', 'd': 'donald'}

y = '&'.join([i + '=' + x[i] for i in x])

print(y)
