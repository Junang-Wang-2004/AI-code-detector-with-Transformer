class C1(object):

    def __init__(self):
        self.indices = []
        self.children = [None] * 26

    def insert(self, a1, a2):
        v1 = self
        for v2 in a1[a2]:
            if not v1.children[ord(v2) - ord('a')]:
                v1.children[ord(v2) - ord('a')] = C1()
            v1 = v1.children[ord(v2) - ord('a')]
            v1.indices.append(a2)

class C2(object):

    def wordSquares(self, a1):
        """
        """
        v1 = []
        v2 = C1()
        for v3 in range(len(a1)):
            v2.insert(a1, v3)
        v4 = []
        for v5 in a1:
            v4.append(v5)
            self.wordSquaresHelper(a1, v2, v4, v1)
            v4.pop()
        return v1

    def wordSquaresHelper(self, a1, a2, a3, a4):
        if len(a3) >= len(a1[0]):
            return a4.append(list(a3))
        v1 = a2
        for v2 in a3:
            v1 = v1.children[ord(v2[len(a3)]) - ord('a')]
            if not v1:
                return
        for v3 in v1.indices:
            a3.append(a1[v3])
            self.wordSquaresHelper(a1, a2, a3, a4)
            a3.pop()
