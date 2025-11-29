class C1(object):

    def findScore(self, a1):
        v1 = len(a1)
        v2 = [False] * v1
        v3 = 0
        v4 = sorted(((a1[j], j) for v5 in range(v1)))
        for v6, v7 in v4:
            if v2[v7]:
                continue
            v2[v7] = True
            v3 += v6
            if v7 > 0:
                v2[v7 - 1] = True
            if v7 < v1 - 1:
                v2[v7 + 1] = True
        return v3
