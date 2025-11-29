from collections import defaultdict

class C1:

    def numSubmatrixSumTarget(self, a1, a2):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        if v1 > v2:
            a1 = list(map(list, zip(*a1)))
            v1, v2 = (v2, v1)
        v4 = []
        for v5 in range(v1):
            v6 = [0] * v2
            for v7 in range(v2):
                v6[v7] = (v6[v7 - 1] if v7 > 0 else 0) + a1[v5][v7]
            v4.append(v6)
        v8 = 0
        for v9 in range(v1):
            v10 = [0] * v2
            for v11 in range(v9, v1):
                for v12 in range(v2):
                    v10[v12] += v4[v11][v12]
                v13 = defaultdict(int)
                v13[0] = 1
                v14 = 0
                for v15 in range(v2):
                    v14 = v10[v15]
                    v8 += v13[v14 - a2]
                    v13[v14] += 1
        return v8
