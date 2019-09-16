import glob, os

def get_files(path = ""):
    if path != "":
        return os.listdir(path)

class directory:
    def __init__(self, from, to):
        self.from = from
        if to is None:
            self.to = self.from
        else:
            self.to = to

    self.files = get_files(self.from)

class file:
    def __init__(self, file_path):
        self.file_path = file_path
