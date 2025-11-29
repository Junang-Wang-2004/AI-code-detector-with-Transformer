class C1:

    def __init__(self):
        self.children = [None] * 26
        self.word_end = False

class C2:

    def __init__(self):
        self.root = C1()

    def insert(self, a1):
        v1 = self.root
        for v2 in a1:
            v3 = ord(v2) - ord('a')
            if v1.children[v3] is None:
                v1.children[v3] = C1()
            v1 = v1.children[v3]
        v1.word_end = True

    def search(self, a1):
        v1 = self._walk(a1)
        return v1 is not None and v1.word_end

    def startsWith(self, a1):
        return self._walk(a1) is not None

    def _walk(self, a1):
        v1 = self.root
        for v2 in a1:
            v3 = ord(v2) - ord('a')
            if v1.children[v3] is None:
                return None
            v1 = v1.children[v3]
        return v1
