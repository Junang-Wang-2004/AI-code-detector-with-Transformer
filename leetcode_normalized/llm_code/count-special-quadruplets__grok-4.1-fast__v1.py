import collections

class C1:

    def countQuadruplets(self, a1):
        v1 = 0
        v2 = collections.Counter()
        v2[a1[-1]] = 1
        v3 = len(a1)
        for v4 in range(v3 - 2, 1, -1):
            v5 = a1[v4]
            for v6 in range(1, v4):
                v7 = v5 + a1[v6]
                for v8 in range(v6):
                    v9 = v7 + a1[v8]
                    v1 += v2[v9]
            v2[a1[v4]] += 1
        return v1
