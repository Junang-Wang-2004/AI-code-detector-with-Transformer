class C1:

    def numberOfCombinations(self, a1: str) -> int:
        v1 = len(a1)
        v2 = 10 ** 9 + 7
        v3 = [[0] * (v1 + 1) for v4 in range(v1 + 1)]
        for v5 in range(v1 - 1, -1, -1):
            for v6 in range(v1 - 1, -1, -1):
                if a1[v5] == a1[v6]:
                    v3[v5][v6] = v3[v5 + 1][v6 + 1] + 1

        def seg_leq(a1: int, a2: int, a3: int) -> bool:
            v1 = v3[a1][a2]
            if v1 >= a3:
                return True
            return a1[a1 + v1] < a1[a2 + v1]
        v7 = [[0] * (v1 + 2) for v4 in range(v1 + 1)]
        v8 = [[0] * (v1 + 2) for v4 in range(v1 + 1)]
        for v9 in range(1, v1 + 1):
            for v10 in range(1, v9 + 1):
                v11 = v9 - v10
                if a1[v11] == '0':
                    v7[v9][v10] = 0
                elif v11 == 0:
                    v7[v9][v10] = 1
                else:
                    v12 = v8[v11][v10 - 1]
                    v13 = 0
                    if v10 <= v11:
                        v14 = v11 - v10
                        if seg_leq(v14, v11, v10):
                            v13 = v7[v11][v10]
                    v7[v9][v10] = (v12 + v13) % v2
                v8[v9][v10] = (v8[v9][v10 - 1] + v7[v9][v10]) % v2
        return v8[v1][v1]
