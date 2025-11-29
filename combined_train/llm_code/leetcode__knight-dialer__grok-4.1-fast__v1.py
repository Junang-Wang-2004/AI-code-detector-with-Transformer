class C1:

    def knightDialer(self, a1: int) -> int:
        v1 = 10 ** 9 + 7
        v2 = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        v3 = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        v4 = [[] for v5 in range(10)]
        for v6 in range(10):
            v7, v8 = v2[v6]
            for v9, v10 in v3:
                v11, v12 = (v7 + v9, v8 + v10)
                if 0 <= v11 <= 3 and 0 <= v12 <= 2 and (v11 < 3 or v12 == 1):
                    v13 = 0 if v11 == 3 else v11 * 3 + v12 + 1
                    v4[v6].append(v13)
        v14 = [1] * 10
        for v5 in range(a1 - 1):
            v15 = [0] * 10
            for v16 in range(10):
                for v13 in v4[v16]:
                    v15[v13] = (v15[v13] + v14[v16]) % v1
            v14 = v15
        return sum(v14) % v1
