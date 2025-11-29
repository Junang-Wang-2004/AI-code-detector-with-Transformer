class C1(object):

    def __init__(self):
        self.files = {'': -1}

    def create(self, a1, a2):
        v1 = '/'.join(a1.split('/')[:-1])
        if v1 not in self.files:
            return False
        self.files[a1] = a2
        return True

    def get(self, a1):
        return self.files.get(a1, -1)
