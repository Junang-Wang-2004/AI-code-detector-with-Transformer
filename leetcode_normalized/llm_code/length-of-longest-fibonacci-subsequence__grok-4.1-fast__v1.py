class C1(object):

    def lenLongestFibSubseq(self, a1):
        v1 = len(a1)
        v2 = {a1[i]: i for v3 in range(v1)}
        v4 = {}
        v5 = 2
        for v6 in range(v1):
            for v3 in range(v6):
                v7 = a1[v6] - a1[v3]
                if v7 in v2:
                    v8 = v2[v7]
                    if v8 < v3:
                        v9 = v4.get((v8, v3), 2)
                        v10 = v9 + 1
                        v4[v3, v6] = v10
                        if v10 > v5:
                            v5 = v10
        return v5 if v5 > 2 else 0
