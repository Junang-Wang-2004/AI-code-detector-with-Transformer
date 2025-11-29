class FileSystem(object):

    def __init__(self):
        self.files = {"": -1}

    def create(self, path, value):
        parent_path = '/'.join(path.split('/')[:-1])
        if parent_path not in self.files:
            return False
        self.files[path] = value
        return True

    def get(self, path):
        return self.files.get(path, -1)
