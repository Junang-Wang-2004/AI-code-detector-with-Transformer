class C1(object):

    def __init__(self):
        self.is_string = False
        self.leaves = {}

class C2(object):

    def __init__(self):
        self.root = C1()

    def insert(self, a1):
        v1 = self.root
        for v2 in a1:
            if not v2 in v1.leaves:
                v1.leaves[v2] = C1()
            v1 = v1.leaves[v2]
        v1.is_string = True

    def search(self, a1):
        v1 = self.childSearch(a1)
        if v1:
            return v1.is_string
        return False

    def startsWith(self, a1):
        return self.childSearch(a1) is not None

    def childSearch(self, a1):
        v1 = self.root
        for v2 in a1:
            if v2 in v1.leaves:
                v1 = v1.leaves[v2]
            else:
                return None
        return v1
