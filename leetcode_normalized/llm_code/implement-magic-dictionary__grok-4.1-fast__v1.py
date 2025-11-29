class C1:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class C2:

    def __init__(self):
        self.root = C1()

    def buildDict(self, a1):
        for v1 in a1:
            v2 = self.root
            for v3 in v1:
                v4 = ord(v3) - ord('a')
                if v2.children[v4] is None:
                    v2.children[v4] = C1()
                v2 = v2.children[v4]
            v2.is_end = True

    def search(self, a1):

        def explore(a1, a2, a3):
            if a1 == len(a1):
                return a2.is_end and a3
            v1 = False
            v2 = ord(a1[a1]) - ord('a')
            if a2.children[v2] is not None:
                if a3:
                    v1 = v1 or explore(a1 + 1, a2.children[v2], True)
                else:
                    v1 = v1 or explore(a1 + 1, a2.children[v2], False)
            if not a3:
                for v3 in range(26):
                    if v3 != v2 and a2.children[v3] is not None:
                        v1 = v1 or explore(a1 + 1, a2.children[v3], True)
            return v1
        return explore(0, self.root, False)
