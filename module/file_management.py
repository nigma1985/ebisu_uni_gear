import glob, os, re, exifread, time, datetime
# from datetime import datetime
# from dateutil import parser
sep = os.path.sep

def get_files(path = ""):
    if path != "":
        return os.listdir(path)

def is_folder(element = ""):
    if element != "":
        return "." not in element

def is_file(element = ""):
    if element != "":
        return "." in element

def is_file_type(element = None, type = None, regex = None):
    if element is None or (type is None and regex is None):
        return None
    elif regex is None and type is not None:
        regex = "\\{}$".format(type)
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
    if do == 1:
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




###############################################################################
###############################################################################

class file:
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
        self.file_path = directory + sep + element
        self.types = types

        self.type, self.tid = self.get_type(in_types = self.types, element = self.file_path)
        self.tags = read_tags(path_name = self.file_path, do = self.tid)
        self.make = key_value(dictionary = self.tags, key = "Image Make")
        self.model = key_value(dictionary = self.tags, key = "Image Model")
        # self.mode, self.ino, self.dev, self.nlink, self.uid, self.gid, self.size, self.atime, self.mtime, self.ctime = os.stat(element)
        self.atime, self.mtime, self.ctime = [
            datetime.datetime.fromtimestamp(os.path.getatime(element)),
            datetime.datetime.fromtimestamp(os.path.getmtime(element)),
            datetime.datetime.fromtimestamp(os.path.getctime(element))]

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
            find_date(string = self.element),
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

    def get_path(self, directory = None):
        if directory is None:
            directory = self.tags
        # elif len(directory) < 1:
        #     return
        else:
            pass

        cam = ""
        date = ""
        model = key_value(dictionary = dictionary, key = "Image Model")
        make = key_value(dictionary = dictionary, key = "Image Make")
        dt_exif_min, dt_exif_max = dt_min_max(dictionary = dictionary)
        dt_file_min, dt_file_max = (None, None) #
        dt_name = None #

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

        date = min(dt_exif_min, dt_file_min, dt_name)

    def move(self, orig, dest):
        print(self.element, orig, dest, self.tid, self.type)
        print("---", self.get_date(), "|", self.make, self.model, "|", self.date_from_name, min(self.atime, self.mtime, self.ctime), self.exif_min_date)

    def auto_move(self, orig = None, dest = None):
        if orig is None:
            orig = self.directory
        if dest is None:
            dest = self.directory

        if self.tid == -1: ## handle folders
            self.move(orig = orig, dest = dest + "_folder")
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

        self.files = get_files(self.orig)

        self.types = types
        self.regex = self.type2regex(regex = regex, types = self.types)

    def get_types(self):
        lst = []
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            lst.append(f.type)
        return lst

    def get_tids(self):
        lst = []
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            lst.append(f.tid)
        return lst

    def get_crt(self):
        lst = []
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            lst.append(f.tid)
        return lst

    def get_tags(self):
        lst = []
        # print(self.types)
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            lst.append(f.tags)
        return lst

    def _listDir(self):
        fls = self.files
        tps = self.get_tids()
        res = [ i for i in range( len(fls)-1 ) if tps == -1 ]
        print(fls, "|", tps, "|", res)
        return res


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
