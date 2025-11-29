class C1(object):

    def wordBreak(self, a1, a2):
        """
        """
        v1 = len(a1)
        v2 = 0
        for v3 in a2:
            v2 = max(v2, len(v3))
        v4 = [False for v5 in range(v1 + 1)]
        v6 = [[False] * v1 for v5 in range(v1)]
        v4[0] = True
        for v7 in range(1, v1 + 1):
            for v8 in range(1, min(v7, v2) + 1):
                if v4[v7 - v8] and a1[v7 - v8:v7] in a2:
                    v6[v7 - v8][v7 - 1] = True
                    v4[v7] = True
        v9 = []
        if v4[-1]:
            self.wordBreakHelper(a1, v6, 0, [], v9)
        return v9

    def wordBreakHelper(self, a1, a2, a3, a4, a5):
        if a3 == len(a1):
            a5.append(' '.join(a4))
            return
        for v1 in range(a3, len(a1)):
            if a2[a3][v1]:
                a4 += [a1[a3:v1 + 1]]
                self.wordBreakHelper(a1, a2, v1 + 1, a4, a5)
                a4.pop()
