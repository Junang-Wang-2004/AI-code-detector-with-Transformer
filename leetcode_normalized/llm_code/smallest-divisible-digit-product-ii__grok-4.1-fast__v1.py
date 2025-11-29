class C1:

    def smallestNumber(self, a1: str, a2: int) -> str:

        def factorize(a1: int) -> list[int]:
            if a1 < 2:
                return []
            v1 = [0] * 4
            v2 = [2, 3, 5, 7]
            for v3, v4 in enumerate(v2):
                while a1 % v4 == 0:
                    v1[v3] += 1
                    a1 //= v4
            return v1 if a1 == 1 else []
        v1 = factorize(a2)
        if not v1:
            return '-1'
        v2 = [[0] * 4 for v3 in range(10)]
        for v4 in range(1, 10):
            v2[v4] = factorize(v4)
        v5 = [int(c) for v6 in a1]
        v7 = len(v5)
        v8 = next((k for v9 in range(v7) if v5[v9] == 0), v7)
        for v9 in range(v8, v7):
            v5[v9] = 1
        v10 = [0] * 4
        for v4 in v5:
            for v11 in range(4):
                v10[v11] += v2[v4][v11]
        if all((v10[v11] >= v1[v11] for v11 in range(4))):
            return ''.join(map(str, v5))

        def get_counts(a1: list[int]) -> list[int]:
            v1, v2, v3, v4 = a1
            v5 = [0] * 8
            v5[6] = v1 // 3
            v6 = v1 % 3
            v5[7] = v2 // 2
            v7 = v2 % 2
            v5[3] = v3
            v5[5] = v4
            if v6 == 2 and v7 == 1:
                v5[0] = 1
                v5[4] = 1
            elif v6 == 2:
                v5[2] = 1
            elif v6 == 1 and v7 == 1:
                v5[4] = 1
            elif v6 == 1:
                v5[0] = 1
            elif v7 == 1:
                v5[1] = 1
            return v5

        def make_suffix(a1: list[int], a2: int) -> str:
            v1 = sum(a1)
            v2 = a2 - v1
            v3 = ['1'] * v2
            for v4 in range(2, 10):
                v3.extend([str(v4)] * a1[v4 - 2])
            return ''.join(v3)
        for v12 in range(v7 - 1, -1, -1):
            v13 = v5[v12]
            for v11 in range(4):
                v10[v11] -= v2[v13][v11]
            for v14 in range(v13 + 1, 10):
                v15 = [v10[v11] + v2[v14][v11] for v11 in range(4)]
                v16 = [max(0, v1[v11] - v15[v11]) for v11 in range(4)]
                v17 = get_counts(v16)
                v18 = v7 - v12 - 1
                if sum(v17) <= v18:
                    v19 = make_suffix(v17, v18)
                    return a1[:v12] + str(v14) + v19
        v16 = [max(0, v1[v11] - v10[v11]) for v11 in range(4)]
        v17 = get_counts(v16)
        return make_suffix(v17, v7 + 1)
