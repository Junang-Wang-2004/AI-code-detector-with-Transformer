from collections import defaultdict

class C1:

    def smallestTrimmedNumbers(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * len(a2)
        v3 = max((trim for v4, v5 in a2))
        v6 = defaultdict(list)
        for v7, (v8, v5) in enumerate(a2):
            v6[v5].append((v8, v7))
        v9 = list(range(v1))
        for v10 in range(1, v3 + 1):
            v11 = [0] * 10
            for v12 in v9:
                v13 = int(a1[v12][-v10])
                v11[v13] += 1
            for v14 in range(1, 10):
                v11[v14] += v11[v14 - 1]
            v15 = [0] * v1
            for v12 in reversed(v9):
                v13 = int(a1[v12][-v10])
                v11[v13] -= 1
                v15[v11[v13]] = v12
            v9 = v15
            if v10 in v6:
                for v8, v7 in v6[v10]:
                    v2[v7] = v9[v8 - 1]
        return v2
