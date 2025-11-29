from collections import defaultdict

class C1:

    def minTransfers(self, a1):
        v1 = defaultdict(int)
        for v2, v3, v4 in a1:
            v1[v2] += v4
            v1[v3] -= v4
        v5 = [amt for v6 in v1.values() if v6 != 0]
        v7 = len(v5)
        if v7 == 0:
            return 0
        v8 = 1 << v7
        v9 = [0] * v8
        for v10 in range(v8):
            for v11 in range(v7):
                if v10 & 1 << v11:
                    v9[v10] += v5[v11]
        v12 = [0] * v8
        for v10 in range(1, v8):
            v13 = 0
            for v11 in range(v7):
                if v10 & 1 << v11:
                    v14 = v10 ^ 1 << v11
                    v13 = max(v13, v12[v14])
            v15 = 1 if v9[v10] == 0 else 0
            v12[v10] = v13 + v15
        return v7 - v12[-1]
