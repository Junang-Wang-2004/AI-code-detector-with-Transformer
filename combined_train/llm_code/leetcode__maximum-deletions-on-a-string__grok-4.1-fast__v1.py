class C1:

    def deleteString(self, a1: str) -> int:
        v1 = len(a1)
        if len(set(a1)) == 1:
            return v1
        v2 = 10 ** 9 + 7
        v3 = 131
        v4 = 10 ** 9 + 9
        v5 = 137
        v6 = [1] * (v1 + 1)
        v7 = [1] * (v1 + 1)
        v8 = [0] * (v1 + 1)
        v9 = [0] * (v1 + 1)
        for v10 in range(v1):
            v11 = ord(a1[v10]) - ord('a') + 1
            v8[v10 + 1] = (v8[v10] * v3 + v11) % v2
            v6[v10 + 1] = v6[v10] * v3 % v2
            v9[v10 + 1] = (v9[v10] * v5 + v11) % v4
            v7[v10 + 1] = v7[v10] * v5 % v4

        def get_h1(a1: int, a2: int) -> int:
            v1 = a2 - a1 + 1
            v2 = (v8[a2 + 1] - v8[a1] * v6[v1] % v2 + v2) % v2
            return v2

        def get_h2(a1: int, a2: int) -> int:
            v1 = a2 - a1 + 1
            v2 = (v9[a2 + 1] - v9[a1] * v7[v1] % v4 + v4) % v4
            return v2
        v12 = [1] * v1
        for v13 in range(v1 - 1, -1, -1):
            v14 = 1
            v15 = (v1 - v13) // 2
            for v16 in range(1, v15 + 1):
                v17 = v13 + v16
                if get_h1(v13, v13 + v16 - 1) == get_h1(v17, v17 + v16 - 1) and get_h2(v13, v13 + v16 - 1) == get_h2(v17, v17 + v16 - 1):
                    v14 = max(v14, 1 + v12[v17])
            v12[v13] = v14
        return v12[0]
