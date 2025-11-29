class C1(object):

    def __init__(self):
        self.is_string = False
        self.leaves = {}

class C2(object):

    def __init__(self):
        self.root = C1()

    def addWord(self, a1):
        v1 = self.root
        for v2 in a1:
            if v2 not in v1.leaves:
                v1.leaves[v2] = C1()
            v1 = v1.leaves[v2]
        v1.is_string = True

    def search(self, a1):
        return self.searchHelper(a1, 0, self.root)

    def searchHelper(self, a1, a2, a3):
        if a2 == len(a1):
            return a3.is_string
        if a1[a2] in a3.leaves:
            return self.searchHelper(a1, a2 + 1, a3.leaves[a1[a2]])
        elif a1[a2] == '.':
            for v1 in a3.leaves:
                if self.searchHelper(a1, a2 + 1, a3.leaves[v1]):
                    return True
        return False
