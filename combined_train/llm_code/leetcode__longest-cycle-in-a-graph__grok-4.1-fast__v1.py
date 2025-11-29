class C1(object):

    def longestCycle(self, a1):
        v1 = len(a1)
        v2 = [False] * v1
        v3 = -1
        for v4 in range(v1):
            if v2[v4]:
                continue
            v5 = {}
            v6 = []
            v7 = v4
            while not v2[v7] and v7 not in v5:
                v5[v7] = len(v6)
                v6.append(v7)
                v7 = a1[v7]
            if v7 in v5:
                v3 = max(v3, len(v6) - v5[v7])
            for v8 in v6:
                v2[v8] = True
        return v3
