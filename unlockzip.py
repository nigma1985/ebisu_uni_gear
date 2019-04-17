import glob, os
from zipfile import ZipFile
from pathlib import Path

from datetime import datetime
from datetime import timedelta
import time

os.chdir("../ebisu_uni_gear/")

zip_file = 'input/Downloads.zip'
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

def run_sec(start, curent):
    return

def run_perf(secs, files):
    return

def brute_unzip(file):
    i = 1
    p = 1
    pw = None
    start_sec = time.mktime(datetime.now().timetuple())

    print('--- --- ---', file, '|', datetime.now(), '--- --- ---')

    while True:
        pw = cnt2str(i)
        now_sec = time.mktime(datetime.now().timetuple())
        try:
            with ZipFile(file) as zf:
                zf.extractall(path = getDir(file), pwd=bytes(pw,'utf-8'))
            print('done! ', i, ' | ', pw)
            print('--- --- ---', file, '|', datetime.now(), '--- --- ---')
            return pw
        except:
            i = i+1
        finally:
            # print(i, '|', pw)
            if i == 2 ** p:
                print('n^'+str(p), '|', i, '|', pw)
                p = p+1


brute_unzip(zip_file)

#
# pw = 'Konrad'
# goes = ''
# while goes != pw:
#     i = i+1
#     goes = cnt2str(i)
#     if i == 2 ** p:
#         p = p+1
#         print('n^'+str(p), '|', i, '|', goes)
#
# print(i, '|', goes, pw)

# path = getDir(zip_file)
#
# print(zip_file, path, password)

# with ZipFile(zip_file) as zf:
#   zf.extractall(path = getDir(zip_file), pwd=bytes(password,'utf-8'))

# # import zipfile
# zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
# zip_ref.extractall(directory_to_extract_to)
# zip_ref.close()
