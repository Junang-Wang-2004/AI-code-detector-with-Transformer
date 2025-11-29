class C1:

    def sameEndSubstringCount(self, a1, a2):
        v1 = len(a1)
        v2 = [[0] * (v1 + 1) for v3 in range(26)]
        for v4, v5 in enumerate(a1):
            v6 = ord(v5) - ord('a')
            for v7 in range(26):
                v2[v7][v4 + 1] = v2[v7][v4]
            v2[v6][v4 + 1] += 1
        v8 = []
        for v9, v10 in a2:
            v11 = 0
            for v7 in range(26):
                v12 = v2[v7][v10 + 1] - v2[v7][v9]
                v11 += v12 * (v12 + 1) // 2
            v8.append(v11)
        return v8
