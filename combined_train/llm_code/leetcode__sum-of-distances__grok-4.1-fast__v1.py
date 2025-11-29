from collections import defaultdict

class C1(object):

    def distance(self, a1):
        v1 = defaultdict(list)
        v2 = len(a1)
        for v3, v4 in enumerate(a1):
            v1[v4].append(v3)
        v5 = [0] * v2
        for v6 in v1.values():
            v7 = len(v6)
            if v7 < 2:
                continue
            v8 = [0] * (v7 + 1)
            for v9 in range(v7):
                v8[v9 + 1] = v8[v9] + v6[v9]
            for v10 in range(v7):
                v11 = v10
                v12 = v8[v10]
                v13 = v11 * v6[v10] - v12
                v14 = v7 - v10 - 1
                v15 = v8[v7] - v8[v10 + 1]
                v16 = v15 - v14 * v6[v10]
                v5[v6[v10]] = v13 + v16
        return v5
