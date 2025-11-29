class C1:

    def countGoodSubsequences(self, a1):
        v1 = 10 ** 9 + 7
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        v4 = max(v2)
        v5 = [1] * (v4 + 1)
        for v6 in range(1, v4 + 1):
            v5[v6] = v5[v6 - 1] * v6 % v1
        v7 = [pow(v5[v6], v1 - 2, v1) for v6 in range(v4 + 1)]

        def choose(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v5[a1] * v7[a2] % v1 * v7[a1 - a2] % v1
        v8 = 0
        for v9 in range(1, v4 + 1):
            v10 = 1
            for v11 in v2:
                v10 = v10 * (1 + choose(v11, v9)) % v1
            v8 = (v8 + v10 - 1) % v1
        return v8
