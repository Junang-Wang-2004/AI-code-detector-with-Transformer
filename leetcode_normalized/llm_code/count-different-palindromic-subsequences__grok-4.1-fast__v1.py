class C1:

    def countPalindromicSubsequences(self, a1: str) -> int:
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = 10 ** 9 + 7
        v3 = [[-1] * 4 for v4 in range(v1)]
        v5 = [[-1] * 4 for v4 in range(v1)]
        for v6 in range(4):
            v7 = -1
            for v8 in range(v1 - 1, -1, -1):
                if ord(a1[v8]) - ord('a') == v6:
                    v7 = v8
                v3[v8][v6] = v7
            v7 = -1
            for v8 in range(v1):
                if ord(a1[v8]) - ord('a') == v6:
                    v7 = v8
                v5[v8][v6] = v7
        v9 = [[0] * v1 for v4 in range(v1)]
        for v10 in range(1, v1 + 1):
            for v11 in range(v1 - v10 + 1):
                v12 = v11 + v10 - 1
                v13 = 1
                for v6 in range(4):
                    v14 = v3[v11][v6]
                    if v14 == -1 or v14 > v12:
                        continue
                    v13 = (v13 + 1) % v2
                    v15 = v5[v12][v6]
                    if v14 < v15:
                        v16 = v14 + 1
                        v17 = v15 - 1
                        if v16 > v17:
                            v13 = (v13 + 1) % v2
                        else:
                            v13 = (v13 + v9[v16][v17]) % v2
                v9[v11][v12] = v13
        return (v9[0][v1 - 1] - 1 + v2) % v2
