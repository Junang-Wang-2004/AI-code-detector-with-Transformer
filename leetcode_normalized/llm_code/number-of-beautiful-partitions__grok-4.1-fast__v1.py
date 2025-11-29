class C1:

    def beautifulPartitions(self, a1: str, a2: int, a3: int) -> int:
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [False] * v2
        v4 = set('2357')
        for v5 in range(v2):
            v3[v5] = a1[v5] in v4
        v6 = [[0] * (a2 + 1) for v7 in range(v2 + 1)]
        v6[0][0] = 1
        for v8 in range(1, a2 + 1):
            v9 = 0
            for v10 in range(1, v2 + 1):
                v11 = v10 - a3
                if v11 >= 0 and v3[v11]:
                    v9 = (v9 + v6[v11][v8 - 1]) % v1
                if a1[v10 - 1] not in v4:
                    v6[v10][v8] = v9
        return v6[v2][a2]
