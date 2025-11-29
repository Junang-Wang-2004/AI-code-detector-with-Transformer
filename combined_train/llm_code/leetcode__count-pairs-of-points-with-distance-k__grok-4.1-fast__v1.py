import collections

class C1(object):

    def countPairs(self, a1, a2):
        v1 = collections.Counter((tuple(p) for v2 in a1))
        v3 = 0
        for v4 in v1:
            v5, v6 = v4
            for v7 in range(a2 + 1):
                v8 = v5 ^ v7
                v9 = v6 ^ a2 - v7
                v10 = (v8, v9)
                if v10 < v4:
                    continue
                v11 = v1[v4]
                v12 = v1[v10]
                if v10 == v4:
                    v3 += v11 * (v11 - 1) // 2
                else:
                    v3 += v11 * v12
        return v3
