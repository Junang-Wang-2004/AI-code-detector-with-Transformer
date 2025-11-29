class C1:

    def countDivisibleSubstrings(self, a1):
        v1 = []
        v2 = ord('a')
        for v3 in a1:
            v4 = ord(v3) - v2
            v1.append((v4 + 1) // 3 + 1)
        v5 = len(v1)
        v6 = 0
        for v7 in range(1, 10):
            v8 = {0: 1}
            v9 = 0
            for v10 in range(v5):
                v9 += v1[v10]
                v11 = v9 - v7 * (v10 + 1)
                v6 += v8.get(v11, 0)
                v8[v11] = v8.get(v11, 0) + 1
        return v6
