class C1(object):

    def findWinners(self, a1):
        v1 = {}
        v2 = []
        for v3, v4 in a1:
            v1[v4] = v1.get(v4, 0) + 1
            v2.extend([v3, v4])
        v5 = sorted(set(v2))
        v6 = []
        v7 = []
        for v8 in v5:
            v9 = v1.get(v8, 0)
            if v9 == 0:
                v6.append(v8)
            elif v9 == 1:
                v7.append(v8)
        return [v6, v7]
