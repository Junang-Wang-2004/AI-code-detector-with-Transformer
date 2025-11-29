class C1:

    def countSubstrings(self, a1: str) -> int:
        v1 = 0
        v2 = len(a1)
        v3 = [[0] * 10 for v4 in range(10)]
        for v5 in range(v2):
            v6 = int(a1[v5])
            v7 = [[0] * 10 for v4 in range(10)]
            for v8 in range(1, 10):
                v7[v8][v6 % v8] += 1
                for v9 in range(v8):
                    v10 = (v9 * 10 + v6) % v8
                    v7[v8][v10] += v3[v8][v9]
            v3 = v7
            v1 += v3[v6][0]
        return v1
