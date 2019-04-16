import glob, os
from zipfile import ZipFile
from pathlib import Path


os.chdir("../ebisu_uni_gear/")

zip_file = 'input/test.zip'
password = 'password'

def getDir(path):
    if path is None:
        return
    return Path(path).parent.absolute()

def cnt2str(cnt):
    if cnt is None or not isinstance(cnt, int):
        return
    sym_list = '0123456789' + 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'äÄöÖüÜß' + '°!§$%&/()=?"`^´²³{[\\]}@€+*~\'#<>|,.-;:_ '
    cur_cnt = cnt % len(sym_list)
    nxt_cnt = (cnt - (cnt % len(sym_list))) / len(sym_list)
    if nxt_cnt > 0:
        return cnt2str(int(nxt_cnt)) + sym_list[cur_cnt -1]
    return sym_list[cur_cnt -1]

i = 0
p = 1
pw = 'Konrad'
goes = ''
while goes != pw:
    i = i+1
    goes = cnt2str(i)
    if i == 2 ** p:
        p = p+1
        print('n^'+str(p), '|', i, '|', goes)

print(i, '|', goes, pw)

# path = getDir(zip_file)
#
# print(zip_file, path, password)

# with ZipFile(zip_file) as zf:
#   zf.extractall(path = getDir(zip_file), pwd=bytes(password,'utf-8'))

# # import zipfile
# zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
# zip_ref.extractall(directory_to_extract_to)
# zip_ref.close()
