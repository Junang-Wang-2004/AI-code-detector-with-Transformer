class C1(object):

    def maxScoreIndices(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in a1:
            v2 += v3
        v4 = 0
        v5 = -1
        v6 = []
        for v7 in range(v1 + 1):
            v8 = v7 - v4
            v9 = v4 + v2 - v8
            if v9 > v5:
                v5 = v9
                v6 = [v7]
            elif v9 == v5:
                v6.append(v7)
            if v7 < v1:
                if a1[v7] == 0:
                    v4 += 1
        return v6
