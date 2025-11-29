class C1(object):

    def maxWeight(self, a1, a2, a3, a4):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
        v6 = [[False] * a4 for v2 in range(a1)]
        for v7 in range(a1):
            v6[v7][0] = True
        for v2 in range(a3):
            v8 = [[False] * a4 for v2 in range(a1)]
            for v3 in range(a1):
                for v9 in range(a4):
                    if v6[v3][v9]:
                        for v4, v10 in v1[v3]:
                            v11 = v9 + v10
                            if v11 < a4:
                                v8[v4][v11] = True
            v6 = v8
        v12 = -1
        for v3 in range(a1):
            for v9 in range(a4 - 1, -1, -1):
                if v6[v3][v9]:
                    v12 = max(v12, v9)
                    break
        return v12
