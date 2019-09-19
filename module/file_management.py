import glob, os

def get_files(path = ""):
    if path != "":
        return os.listdir(path)

def is_folder(element = ""):
    if element != "":
        return "." not in element

def is_file(element = ""):
    if element != "":
        return "." in element


class file:
    def __init__(self, directory = None, element = None, types = []):
        self.directory = directory
        self.element = element

        # self.file_path = directory + "\\" + element

        if is_folder(element = element):
            self.type = "folder"
            self.tid = -1
        elif types is None:
            self.type = None
            self.tid = None
        # elif isinstance(types, [list, tuple]) and len(types) > 0:
        #     self.type = None
        else:
            self.type = "other"
            self.tid = 0
            for type in types:
                if type in element:
                    self.type = type
                    self.tid = 1
                else:
                    pass

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


class drcty:
    def __init__(self, orig = None, dest = None, types = []):
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
            lst.append(f.type)
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
