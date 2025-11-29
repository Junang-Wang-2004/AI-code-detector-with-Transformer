class C1(object):

    def __init__(self):
        self.is_string = False
        self.leaves = {}

    def insert(self, a1):
        v1 = self
        for v2 in a1:
            if not v2 in v1.leaves:
                v1.leaves[v2] = C1()
            v1 = v1.leaves[v2]
        v1.is_string = True

class C2(object):

    def findWords(self, a1, a2):
        """
        """
        v1 = [[False for v2 in range(len(a1[0]))] for v3 in range(len(a1))]
        v4 = {}
        v5 = C1()
        for v6 in a2:
            v5.insert(v6)
        for v3 in range(len(a1)):
            for v2 in range(len(a1[0])):
                self.findWordsRecu(a1, v5, 0, v3, v2, v1, [], v4)
        return list(v4.keys())

    def findWordsRecu(self, a1, a2, a3, a4, a5, a6, a7, a8):
        if not a2 or a4 < 0 or a4 >= len(a1) or (a5 < 0) or (a5 >= len(a1[0])) or a6[a4][a5]:
            return
        if a1[a4][a5] not in a2.leaves:
            return
        a7.append(a1[a4][a5])
        v1 = a2.leaves[a1[a4][a5]]
        if v1.is_string:
            a8[''.join(a7)] = True
        a6[a4][a5] = True
        self.findWordsRecu(a1, v1, a3 + 1, a4 + 1, a5, a6, a7, a8)
        self.findWordsRecu(a1, v1, a3 + 1, a4 - 1, a5, a6, a7, a8)
        self.findWordsRecu(a1, v1, a3 + 1, a4, a5 + 1, a6, a7, a8)
        self.findWordsRecu(a1, v1, a3 + 1, a4, a5 - 1, a6, a7, a8)
        a6[a4][a5] = False
        a7.pop()
