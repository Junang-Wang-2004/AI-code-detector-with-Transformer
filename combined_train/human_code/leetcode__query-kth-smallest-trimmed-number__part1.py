class C1(object):

    def smallestTrimmedNumbers(self, a1, a2):
        """
        """
        v1 = max((t for v2, v3 in a2))
        v4 = [[] for v2 in range(v1 + 1)]
        for v5, (v6, v3) in enumerate(a2):
            v4[v3].append((v6, v5))
        v7 = [0] * len(a2)
        v8 = list(range(len(a1)))
        for v9 in range(1, v1 + 1):
            v10 = [0] * 10
            for v5 in v8:
                v11 = int(a1[v5][-v9])
                v10[v11] += 1
            for v11 in range(9):
                v10[v11 + 1] += v10[v11]
            v12 = [0] * len(a1)
            for v5 in reversed(v8):
                v11 = int(a1[v5][-v9])
                v10[v11] -= 1
                v12[v10[v11]] = v5
            v8 = v12
            for v6, v5 in v4[v9]:
                v7[v5] = v8[v6 - 1]
        return v7
