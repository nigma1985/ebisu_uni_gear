import glob, os
from zipfile import ZipFile
from pathlib import Path

from datetime import datetime
from datetime import timedelta
import time

os.chdir("/home/pi/ebisu_uni_gear/")

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
    print(curent, start, secs)

    if 1.1 < (secs / (60 * 60 * 24 * 365.2425)): ## Year
        return '{9.3f}Y'.format(secs / (60 * 60 * 24 * 365.2425))
    elif 1.1 < (secs / (60 * 60 * 24 * (365.2425 /  4))): ## Quarters
        return '{9.3f}Q'.format(secs / (60 * 60 * 24 * (365.2425 /  4)))
    elif 1.1 < (secs / (60 * 60 * 24 * (365.2425 / 12))): ## Months
        return '{9.3f}mon'.format(secs / (60 * 60 * 24 * (365.2425 / 12)))
    elif 1.1 < (secs / (60 * 60 * 24 * 7)): ## weeks
        return '{9.3f}w'.format(secs / (60 * 60 * 24 * 7))
    elif 1.1 < (secs / (60 * 60 * 24)): ## days
        return '{9.3f}d'.format(secs / (60 * 60 * 24))
    elif 1.1 < (secs / (60 * 60)): ## hours
        return '{9.3f}h'.format(secs / (60 * 60))
    elif 1.1 < (secs / (60)): ## minutes
        return '{9.3f}min'.format(secs / (60))
    else: ## seconds (default)
        return '{9.3f}Y'.format(secs)

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
            print('done! ', i, ' | ', pw, '(', run_sec(start_sec, now_sec), '::', run_perf(start_sec, now_sec, i), 'tries/sec)')
            print('--- --- ---', file, '|', datetime.now(), '--- --- ---')
            return pw
        except:
            i = i+1
        finally:
            # print(i, '|', pw)
            if (i == 2 ** p) :
                print('n^'+str(p), '|', i, '|', pw, '(', run_sec(start_sec, now_sec), '::', run_perf(start_sec, now_sec, i), 'tries/sec)')
                p = p+1


brute_unzip(zip_file)
