import collections

class C1:

    def threeSumMulti(self, a1, a2):
        v1 = collections.Counter(a1)
        v2 = list(v1)
        v3 = 0
        v4 = 10 ** 9 + 7
        v5 = len(v2)
        for v6 in range(v5):
            for v7 in range(v6, v5):
                v8 = v2[v6]
                v9 = v2[v7]
                v10 = a2 - v8 - v9
                if v10 not in v1:
                    continue
                v11 = v1[v8]
                v12 = v1[v9]
                v13 = v1[v10]
                if v8 == v9 == v10:
                    v3 += v11 * (v11 - 1) * (v11 - 2) // 6
                elif v8 == v9:
                    v3 += v11 * (v11 - 1) // 2 * v13
                elif max(v8, v9) < v10:
                    v3 += v11 * v12 * v13
        return v3 % v4
