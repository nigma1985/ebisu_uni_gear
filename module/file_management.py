import glob, os, re, exifread, time, datetime
import module.file_management as fm
# from datetime import datetime
# from dateutil import parser
sep = os.path.sep

import numpy as np
# import pandas as pd
# import scipy as spy
from sklearn.linear_model import LinearRegression

def get_files(path = ""):
    if path != "":
        return os.listdir(path)

def is_folder(element = ""):
    if element:
        return "." not in element

def is_file(element = ""):
    if element:
        return "." in element

def is_file_type(element = None, type = None, regex = None):
    if element is None or (type is None and regex is None):
        return None
    elif regex is None and type is not None:
        regex = "{}$".format(type)
    else:
        pass
    return re.search(regex, element, re.IGNORECASE)

def contains_date(element = None):
    if element is None:
        return None
    elif regex is None and type is not None:
        regex = "\\{}$".format(type)
    else:
        pass
    return re.search(regex, element, re.IGNORECASE)

def read_tags(path_name = None, do = 1):
    if True: #do >= 0:
        try:
            f = open(path_name, 'rb')
            return exifread.process_file(f, details=True)
        except:
            return None
    else:
        return None

def key_value(dictionary = {}, key = None):
    try:
        return dictionary[key]
    except:
        return None

def dt_min_max(dictionary = {}, key = "Date"):
    result = [(d, dictionary[d]) for d in dictionary if key in dictionary]
    return (result, result)

def find_date(string = None):
    regex_time = "((0[0-9]|1[0-9]|2[0-3]\\W?[0-5][0-9])(\\W?[0-5][0-9])?)"
    regex_date = "(((19|20)([2468][048]|[13579][26]|0[48])|2000)\\W?02\\W?29|((19|20)[0-9]{2}\\W?(0[469]|11)\\W?(0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}\\W?(0[13578]|1[02])\\W?(0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}\\W?02\\W?(0[1-9]|1[0-9]|2[0-8])))"
    regex = "\\D?({}\\D?({})?)\\D?".format(regex_date, regex_time)
    found = None

    try:
        # print("00", found)
        found = re.search(regex, str(string), re.IGNORECASE)
        # print("01", found)
        if found:
            # return parser.parse(found.group(1)) ### only date/time with symbols in between
            ### add other string types
            found = re.sub(r'\D', "", found.group(1))
            # print("02", found, len(found))
            if len(found) == 14:
                # print(datetime.datetime.strptime(found, '%Y%m%d%H%M%S'))
                return datetime.datetime.strptime(found, '%Y%m%d%H%M%S')
                # pass
            elif len(found) == 12:
                # print(datetime.datetime.strptime(found, '%Y%m%d%H%M'))
                return datetime.datetime.strptime(found, '%Y%m%d%H%M')
                # found = found + "00"
            # elif len(found) == 10:
            #     found = found + "0000"
            elif len(found) == 8:
                # print(datetime.datetime.strptime(found, '%Y%m%d'))
                return datetime.datetime.strptime(found, '%Y%m%d')
                # found = found + "000000"
            else:
                pass
            # print("03", found)

            # return datetime.strptime(found, '%Y%m%d%H%M%S')
        else:
            return None
    except:
        # print("xx", found)
        return None

def extract_list(input = None, output = None):
    if input:
        pass
    else:
        return

    result = []

    if isinstance(input, dict):
        for item in input:
            for i in input[item]:
                result.append(i)
    else:
        return
    return result

def first(item_list):
    if item_list:
        return item_list[0]
    else:
        return None

def last(item_list):
    if item_list:
        return item_list[-1]
    else:
        return None

def clean_list(attr_list = []):
    attr = []
    for item in attr_list:
        if item:
            attr.append(item)
        else:
            pass

    return attr

def get_attr(attr_list = []):
    # attr = []
    # for item in attr_list:
    #     if item:
    #         attr.append(item)
    #     else:
    #         pass
    attr = attr_list
    try:
        attr.sort()
    except:
        try:
            [str(item) for item in attr].sort()
        except:
            return None

    attr_f = first(attr)

    return attr_f if attr_f == last(attr) else None

def get_moda(attr_list = []):
    # attr = []

    # for item in attr_list:
    #     if item:
    #         attr.append(item)
    #     else:
    #         pass
    attr = attr_list
    attr_sets = []
    attr_dict = {}

    if attr:
        attr_sets = set(attr)
    else:
        return


    for key in attr_sets:
        attr_dict[key] = attr.count(key)

    if attr_dict and isinstance(attr_dict, dict):
        attr_len = 0
        for key, value in attr_dict.items():
            if value > 0.5 * len(attr):
                return key
            else:
                pass
        return
        #     attr_len = value if value > attr_len else attr_len
        # return attr_len if attr_len > 0.5 * len(attr) else None
    else:
        return
    # return attr_dict if attr_dict else None

def get_regr(attr_list = []):
    if not attr_list:
        return
    elif len(attr_list) == 1:
        return True
    else:
        pass

    attr = attr_list
    attr.sort()
    cnt, diff = [], []
    for n in range( 1, len(attr) ):
        cnt.append(n)
        diff.append(attr[n] - attr[n-1])

    x = np.array(cnt).reshape((-1, 1))
    y = np.array(diff)

    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)

    return r_sq #> .5

def extract_dict(dict_list = [], key = None):
    result = []
    for row in dict_list:
        try:
            result.append(row[key])
        except:
            pass
    return result

def extract(dict_list = [], key = None):
    result = []
    for row in dict_list:
        try:
            result.append(row[key])
        except:
            pass
    return result

###############################################################################
###############################################################################

class file:
    def get_from_many(self, objt_list = [], attr_list = [], key = None):
        result, extract_list = None, None
        if attr_list:
            extract_list = clean_list(attr_list = attr_list)
        else:
            if objt_list or key:
                extract_list = extract(dict_list = objt_list, key = key)
            else:
                return None
            extract_list = clean_list(attr_list = extract_list)

        if not extract_list:
            return None
        elif len(extract_list) == 1:
            return extract_list[0]
        else:
            result = get_attr(attr_list = extract_list)
            return result if result else get_moda(attr_list = extract_list)

    def get_type(self, in_types = [], element = None):
        if is_folder(element = element):
            # print('folder')
            return ["folder", -1]
        elif in_types is None:
            # print('nothing')
            return [None, None]
        else:
            for type in in_types:
                # if type in element:
                if is_file_type(element = element, type = type):
                    # print('type')
                    return [type, 1]
                    # self.tags = read_tags(path_name = self.file_path)
                else:
                    pass
            # print('other')
            return ["other", 0]

    def __init__(self, directory = None, element = None, types = []):
        self.directory = directory
        self.element = element
        self.file_path = "{}{}{}".format(self.directory, sep, self.element)
        self.types = types

        self.type, self.tid = self.get_type(in_types = self.types, element = self.element)

        # folder = drcty(orig = self.file_path, dest = self.directory) if self.tid == -1 else None
        # print('tid:', self.tid, self.file_path)
        # self.folder = folder.allDict() if folder else None
        self.folder = drcty(orig = self.file_path, dest = self.directory, types = self.types) if self.tid < 0 else None

        self.tags = read_tags(path_name = self.file_path, do = self.tid)
        self.make, self.model = None, None
        if self.tid < 0:
            self.make = self.get_from_many(attr_list = [str(self.folder.files[f].make) for f in self.folder.files if self.folder.files[f].make])
            self.model = self.get_from_many(attr_list = [str(self.folder.files[f].model) for f in self.folder.files if self.folder.files[f].model])
        else:
            self.make = key_value(dictionary = self.tags, key = "Image Make")
            self.model = key_value(dictionary = self.tags, key = "Image Model")
        # self.make = self.get_from_many(attr_list = [self.folder.files[f].make for f in self.folder.files]) if self.tid < 0 else key_value(dictionary = self.tags, key = "Image Make")
        # self.model = self.get_from_many(attr_list = [self.folder.files[f].model for f in self.folder.files]) if self.tid < 0 else key_value(dictionary = self.tags, key = "Image Model")
        # self.mode, self.ino, self.dev, self.nlink, self.uid, self.gid, self.size, self.atime, self.mtime, self.ctime = os.stat(element)
        self.atime, self.mtime, self.ctime = [
            datetime.datetime.fromtimestamp(os.path.getatime(self.file_path)),
            datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path)),
            datetime.datetime.fromtimestamp(os.path.getctime(self.file_path))]

        exif_dates = None
        if self.tags is None:
            pass
        elif len(self.tags) == 0:
            pass
        else:
            exif_dates = [ self.tags[entry] for entry in self.tags if "Date" in entry ]  ### raw date-texts
            if len(exif_dates) == 0:
                exif_dates = None
            else:
                exif_dates = [find_date(string = item) for item in exif_dates]

        self.date_from_name, self.exif_min_date, self.exif_max_date = [  ### dates from texts
            find_date(string = self.file_path),
            min(exif_dates) if exif_dates else None,
            max(exif_dates) if exif_dates else None
            ]

    def get_date(self):
        if self.date_from_name:
            return self.date_from_name
        elif self.exif_min_date:
            return self.exif_min_date
        elif self.atime is not None or self.mtime is not None or self.ctime is not None:
            return min(self.atime, self.mtime, self.ctime)
        else:
            return None

    def _findDate_in_Dir(self, directory = None, date = None):
        if date is None:
            date = self.get_date()
        else:
            pass

        if directory is None:
            directory = self.directory
        else:
            pass

        drcty = fm.drcty(orig = directory)
        list_dir = drcty._listDir()

        for dir in list_dir:
            if re.search("^{}".format(date.strftime('%Y-%m-%d')), dir, re.IGNORECASE):
            # if date.strftime('%Y-%m-%d') in dir:
                return dir
            else:
                pass

        return None

    def get_path(self, directory = None):
        if directory is None:
            directory = self.directory
        # elif len(directory) < 1:
        #     return
        else:
            pass

        cam = ""
        date = ""
        model = self.model
        make = self.make

        if model is not None and make is not None:
            cam = "{} {}".format(make, model)
        elif model is None and make is None:
            cam = ""
        elif model is None:
            cam = make
        elif make is None:
            cam = model
        else:
            pass

        # cam = " ".join([make, model])
        cam = "{}{}".format(sep, cam) if cam is not None or cam != "" else ""

        date = self._findDate_in_Dir()
        if date:
            pass
        else:
            date = self.get_date().strftime('%Y-%m-%d')
        date = "{}{}".format(sep, date) if date is not None or date != "" else ""

        # return str(directory) + str(date) + str(cam) + str(self.element)
        res1 = "{}".format(sep).join([directory, date, cam])
        res2 = None
        if res1:
            while res1 != res2:
                res2 = res1
                res1 = res2.replace("{}{}".format(sep, sep), "{}".format(sep))
            return res1
        else:
            return

    def move(self, orig, dest):
        print(self.element, orig, dest, self.tid, self.type)
        print("---", self.get_date(), "|", self.make, self.model, "|", self.date_from_name, min(self.atime, self.mtime, self.ctime), self.exif_min_date)

    def auto_move(self, orig = None, dest = None):
        if orig is None:
            orig = self.directory
        if dest is None:
            dest = self.directory

        if self.tid == -1: ## handle folders
            regex_date = "(((19|20)([2468][048]|[13579][26]|0[48])|2000)\\-02\\-29|((19|20)[0-9]{2}\\-(0[469]|11)\\-(0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}\\-(0[13578]|1[02])\\-(0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}\\-02\\-(0[1-9]|1[0-9]|2[0-8])))"
            found = None

            try:
                # print("00", found)
                found = re.search("^{}(\\ \\-\\ )?".format(regex_date), str(self.element), re.IGNORECASE)
            except:
                pass

            folder = drcty(orig = "{}{}{}".format(self.directory, sep, self.element), dest = self.directory)
            folder = folder.allDict()
            model = extract_list(input = folder, output = 'model')
            make = extract_list(input = folder, output = 'make')
            atime = extract_list(input = folder, output = 'atime')
            mtime = extract_list(input = folder, output = 'mtime')
            ctime = extract_list(input = folder, output = 'ctime')
            xtime = []
            min_time, max_time = None
            if atime and mtime and ctime:
                for n in range( len(ctime)-1 ):
                    xtime.append(min(atime[n], mtime[n], ctime[n]))
                min_time, max_time = min(xtime), max(xtime)

            if found: ## foldername already has date
                pass ## don't move
            elif True: ## folder contains image series
                return
                # pass ## move entire folder (use details from images)
            else:
                pass ## move file by file

            self.move(orig = orig, dest = self.get_path())
        elif self.tid == 1: ## handle file
            self.move(orig = orig, dest = dest)
        else:
            pass

###############################################################################
###############################################################################

class drcty:
    def type2regex(self, regex = None, types = None):
        if regex is None or len(regex) != len(types):
            return ["\\{}$".format(type) for type in types]
        else:
            return regex

    def __init__(self, orig = None, dest = None, types = [], regex = []):
        if drcty is None:
            self.orig = os.getcwd()
        else:
            self.orig = orig

        if dest is None:
            self.dest = self.orig
        else:
            self.dest = dest

        self.types = types
        self.regex = self.type2regex(regex = regex, types = self.types)

        self.files = {}
        for f in get_files(self.orig):
            # print('file:', self.orig, type(self.orig), f, type(f))
            self.files[f] = file(directory = self.orig, element = f, types = self.types)

    def get_types(self):
        lst = []
        for f in self.files:
            lst.append(self.files[f].type)
        return lst

    def get_tids(self):
        lst = []
        for f in self.files:
            lst.append(self.files[f].tid)
        return lst

    def get_crt(self):
        lst = []
        for f in self.files:
            lst.append(self.files[f].tid)
        return lst

    def get_tags(self):
        lst = []
        for f in self.files:
            lst.append(self.files[f].tags)
        return lst

    def _listDir(self):
        # fls = [key for key in self.files]
        # tps = self.get_tids()
        # res = [ fls[i] for i in range( len(fls)-1 ) if tps[i] == -1 ]
        # print(fls, "|", tps, "|", res)
        res = []
        for f in self.files:
            res.append(f if self.files[f].tid < 0 else None)
        return res

    def allDict(self):
        fls = [key for key in self.files]
        _dictionary = {}
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            _dictionary[elem] = {
                'directory': f.directory,
                'element': f.element,
                'file_path': f.file_path,
                'types': f.types,
                'type': f.type,
                'tid': f.tid,
                'tags': f.tags,
                'make': f.make,
                'model': f.model,
                'atime': f.atime,
                'mtime': f.mtime,
                'ctime': f.ctime,
                'date_from_name': f.date_from_name,
                'exif_min_date': f.exif_min_date,
                'exif_max_date': f.exif_max_date,
                'get_date': f.get_date(),
                '_findDate_in_Dir': f._findDate_in_Dir(),
                'get_path': f.get_path()
            }
        return _dictionary

    def move_one(self, orig, elem, dest):
        f = file(directory = orig, element = elem, types = self.types)
        f.auto_move(dest = dest)

    def move_all(self, orig = None, files = None, dest = None):
        if orig is None:
            orig = self.orig
        if files is None or len(file) == 0:
            files = self.files
        if dest is None:
            dest = self.dest

        for elem in files:
            self.move_one(orig = orig, elem = elem, dest = dest)
            # print(e, "/", len(files)-1, " || ", round(e/(len(files)-1)*100,1), "%")
