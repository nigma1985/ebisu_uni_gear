import glob, os, re, exifread
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

def read_tags(path_name = None):
    f = open(path_name, 'rb')
    return exifread.process_file(f, details=True)

def key_value(dictionary = {}, key = None):
    try:
        return dictionary[key]
    except:
        return None

def dt_min_max(dictionary = {}, key = "Date"):
    result = [(d, dictionary[d]) for d in dictionary if key in dictionary]
    return (result, result)

###############################################################################
###############################################################################

class file:
    def get_type(self, in_types = [], element = None):
        if is_folder(element = element):
            return ("folder", -1)
        elif types is None:
            return (None, None)
        else:
            for type in types:
                # if type in element:
                if is_file_type(element = element, type = type):
                    return (type, 1)
                    # self.tags = read_tags(path_name = self.file_path)
                else:
                    pass
            return ("other", 0)


    def __init__(self, directory = None, element = None, types = []):
        self.directory = directory
        self.element = element
        self.file_path = directory + sep + element

        self.tags = None
        # self.model = None
        # self.make = None
        # self.dt_min = None
        # self.mt_max = None

        # if is_folder(element = element):
        #     self.type = "folder"
        #     self.tid = -1
        # elif types is None:
        #     self.type = None
        #     self.tid = None
        #     # self.tags = read_tags(path_name = self.file_path)
        # # elif isinstance(types, [list, tuple]) and len(types) > 0:
        # #     self.type = None
        # else:
        #     self.type = "other"
        #     self.tid = 0
        #     for type in types:
        #         # if type in element:
        #         if is_file_type(element = element, type = type):
        #             self.type = type
        #             self.tid = 1
        #             self.tags = read_tags(path_name = self.file_path)
        #         else:
        #             pass

        self.type, self.tid = self.get_type(in_types = self.types, element = self.file_path)
        
        if self.tags is None:
            pass
        elif len(self.tags) == 0:
            self.tags = None
        else:
            pass
            # self.model = key_value(dictionary = self.tags, key = "Image Model")
            # self.make = key_value(dictionary = self.tags, key = "Image Make")
            # self.dt_min, self.dt_max = dt_min_max(dictionary = self.tags)

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

    def get_crt(self):
        lst = []
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            lst.append(f.tid)
        return lst

    def get_tags(self):
        lst = []
        for elem in self.files:
            f = file(directory = self.orig, element = elem, types = self.types)
            lst.append(f.tags)
        return lst

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
