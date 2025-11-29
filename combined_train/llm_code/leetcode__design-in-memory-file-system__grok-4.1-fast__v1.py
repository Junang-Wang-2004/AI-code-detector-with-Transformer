class C1:

    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ''

class C2:

    def __init__(self):
        self.root = C1()

    def _split_path(self, a1):
        if a1 == '/':
            return []
        v1 = a1.split('/')[1:]
        return [comp for v2 in v1 if v2]

    def _navigate(self, a1, a2=False):
        v1 = self._split_path(a1)
        v2 = self.root
        for v3 in v1:
            if a2 and v3 not in v2.children:
                v2.children[v3] = C1()
            v2 = v2.children[v3]
        return v2

    def ls(self, a1):
        v1 = self._split_path(a1)
        v2 = self._navigate(a1, False)
        if v2.is_file:
            return [v1[-1]]
        return sorted(v2.children.keys())

    def mkdir(self, a1):
        v1 = self._navigate(a1, True)
        v1.is_file = False

    def addContentToFile(self, a1, a2):
        v1 = self._navigate(a1, True)
        v1.is_file = True
        v1.content += a2

    def readContentFromFile(self, a1):
        v1 = self._navigate(a1, False)
        return v1.content
