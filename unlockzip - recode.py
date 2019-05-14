import glob, os, sys
from zipfile import ZipFile
from pathlib import Path

# import module.files as fls

from datetime import datetime
from datetime import timedelta
import time

from random import sample, randint
start_time = time.mktime(datetime.now().timetuple())

# os.chdir("/home/pi/ebisu_uni_gear/")
os.chdir("../ebisu_uni_gear/")


class unzip:
    def getDir(self, path):
        if path is None:
            return
        return Path(path).parent.absolute()

    def cnt2str(self, cnt):
        if cnt is None:
            return None
        elif not isinstance(cnt, int):
            return None
        elif cnt <= 0:
            return None
        else:
            pass

        sym_list = '0123456789' + 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'äÄöÖüÜß' + '°!§$%&/()=?"`^´²³{[\\]}@€+*~\'#<>|,.-;:_ '
        cur_cnt = cnt % len(sym_list)
        nxt_cnt = (cnt - (cnt % len(sym_list))) / len(sym_list)
        if nxt_cnt > 0:
            return self.cnt2str(int(nxt_cnt)) + sym_list[cur_cnt -1]
        return sym_list[cur_cnt -1]

    def run_sec(self, start, current):
        secs = current - start
        # print(curent, start, secs)
        # print(type(curent), type(start), type(secs))

        if 1.1 < (secs / (60 * 60 * 24 * 365.2425)): ## Year
            return 'Y', secs / (60 * 60 * 24 * 365.2425), secs
        elif 1.1 < (secs / (60 * 60 * 24 * (365.2425 /  4))): ## Quarters
            return 'Q', secs / (60 * 60 * 24 * (365.2425 /  4)), secs
        elif 1.1 < (secs / (60 * 60 * 24 * (365.2425 / 12))): ## Months
            return 'mon', secs / (60 * 60 * 24 * (365.2425 / 12)), secs
        elif 1.1 < (secs / (60 * 60 * 24 * 7)): ## weeks
            return 'w', secs / (60 * 60 * 24 * 7), secs
        elif 1.1 < (secs / (60 * 60 * 24)): ## days
            return 'd', secs / (60 * 60 * 24), secs
        elif 1.1 < (secs / (60 * 60)): ## hours
            return 'h', secs / (60 * 60), secs
        elif 1.1 < (secs / (60)): ## minutes
            return 'min', secs / 60, secs
        else: ## seconds (default)
            return 'sec', secs, secs

    def run_perf(self, time = 0, files = None):
        if time is None or files is None or not isinstance(files, (int, float)):
            return None
        else:
            if time == 0:
                if self.secs not in (0, None):
                    time = self.secs
                else:
                    time = 1/ (10**10)
            else:
                pass

            if files == 0:
                if self.progress not in (0, None):
                    files = self.progress
                else:
                    files = -1* (10**10)
            else:
                pass

            return {'sec/n': time / files, 'n/sec': files / time}

    # Initializer / Instance Attributes
    def __init__(self,
        zipfile = None,
        start = time.mktime(datetime.now().timetuple()),
        password = None,
        passnum = None,
        passnum0 = 0):

        self.zipfile = None
        if zipfile is not None:
            self.zipfile = zipfile
        else:
            raise

        self.start = None
        if start is not None:
            self.start = start

        self.password = None
        if password is not None:
            self.password = password

        self.passnum = None
        if passnum is not None:
            self.passnum = passnum

        self.passnum0 = None
        if passnum0 is not None:
            self.passnum0 = passnum0

        self.zipDir = self.getDir(self.zipfile)
        self.current = time.mktime(datetime.now().timetuple())
        self.timemeasure, self.timelength, self.secs = self.run_sec(start = self.start, current = self.current)
        self.progress = self.passnum - self.passnum0
        self.perf = self.run_perf(time = self.secs, files = self.progress)

        if self.password is None and self.passnum is not None:
            self.password = self.cnt2str(self.passnum)

    # def logResult(self, path, file_name, tst)





    def unzip_file(self):
        try:
            with ZipFile(self.zipfile) as zf:
                if i == 0:
                    zf.extractall(path = self.zipDir)
                else:
                    zf.extractall(path = self.zipDir, pwd=bytes(self.password,'utf-8'))
            return True
        except:
            return False
        # finally:

    def report(self, files = None):
        # if files is not None:
        #     perf = self.run_perf(files = files)
        # else:
        #     perf = self.run_perf(files = self.progress)

        return ">> {} >> {}  ( {} digits :: {}{} :: {} {})  {}".format(
            self.passnum,
            self.password,
            len(self.password),
            round(self.timelength,1),
            self.timemeasure,
            round(self.perf['n/sec'],1),
            'n/sec',
            datetime.now())


def brute_unzip(file = None, p = 0):
    ##

    p_start = p

    pw = None
    list_pw = []
    start_sec = time.mktime(datetime.now().timetuple())
    pw0 = None
    nmin = 1/3*10000

    print('--- --- ---', file, '|', datetime.now(), '--- --- ---')

    while True:
        zipper = unzip(zipfile = zip_file, start = start_sec, passnum = p, passnum0 = p_start)

        if zipper.unzip_file():
            print('success:', zipper.password)
            print(zipper.report())
            print('--- --- ---', zip_file, '--- --- ---')
            print('files put here:', zipper.zipDir)
            sys.exit()
        else:
            # print(nmin)
            if randint(1,int(nmin * 5)) == 1:
            # if randint(1,1000) == 1:
                print(list_pw)
                print(zipper.report())
                list_pw = []
                nmin = zipper.perf['n/sec'] * 60
                # print(nmin * 3)
            else:
                list_pw.append(zipper.password)
                try:
                    list_pw = sample(list_pw, 10)
                except:
                    pass
            p = p+1


    print(zipper.report(files = 100))


zip_file = 'C:/Users/Konrad/OneDrive/E-Mail-Anhänge/DEÜV_Meldung_2018_01_917400_Container.ZIP'
# password = 'password'


brute_unzip(zip_file, 4086898540)
