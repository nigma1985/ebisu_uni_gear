import glob, os
from zipfile import ZipFile
from pathlib import Path

from datetime import datetime
from datetime import timedelta
import time

os.chdir("/home/pi/ebisu_uni_gear/")
# os.chdir("../ebisu_uni_gear/")

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
    secs = curent - start
    # print(curent, start, secs)
    # print(type(curent), type(start), type(secs))

    if 1.1 < (secs / (60 * 60 * 24 * 365.2425)): ## Year
        return '{}Y'.format(round(secs / (60 * 60 * 24 * 365.2425),1))
    elif 1.1 < (secs / (60 * 60 * 24 * (365.2425 /  4))): ## Quarters
        return '{}Q'.format(round(secs / (60 * 60 * 24 * (365.2425 /  4)),1))
    elif 1.1 < (secs / (60 * 60 * 24 * (365.2425 / 12))): ## Months
        return '{}mon'.format(round(secs / (60 * 60 * 24 * (365.2425 / 12)),1))
    elif 1.1 < (secs / (60 * 60 * 24 * 7)): ## weeks
        return '{}w'.format(round(secs / (60 * 60 * 24 * 7),1))
    elif 1.1 < (secs / (60 * 60 * 24)): ## days
        return '{}d'.format(round(secs / (60 * 60 * 24),1))
    elif 1.1 < (secs / (60 * 60)): ## hours
        return '{}h'.format(round(secs / (60 * 60),1))
    elif 1.1 < (secs / (60)): ## minutes
        return '{}min'.format(round(secs / (60),1))
    else: ## seconds (default)
        return '{}sec'.format(round(secs,1))

def run_perf(start, curent, files):
    secs = curent - start
    return secs / files

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
            print(run_sec(start_sec, now_sec), '::', run_perf(start_sec, now_sec, i), 'tries/sec')
            print('--- --- ---', file, '|', datetime.now(), '--- --- ---')
            return pw
        except:
            i = i+1
        finally:
            # print(i, '|', pw)
            if (i == 2 ** p):
                print('n^'+str(p), '|', i, '|', pw, '(', run_sec(start_sec, now_sec), '::', run_perf(start_sec, now_sec, i), 'pw/sec)')
                p = p+1
            # if  ((now_sec - start_sec) % (60 * 60) < 1):
            #     pass



brute_unzip(zip_file)
