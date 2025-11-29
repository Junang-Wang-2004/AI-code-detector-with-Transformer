class C1:

    def dieSimulator(self, a1: int, a2: List[int]) -> int:
        v1 = 10 ** 9 + 7
        v2 = [[0] * a2[i] for v3 in range(6)]
        for v3 in range(6):
            if a2[v3] > 0:
                v2[v3][0] = 1
        for v4 in range(a1 - 1):
            v5 = [sum(v2[v3]) % v1 for v3 in range(6)]
            v6 = sum(v5) % v1
            v7 = [[0] * a2[v3] for v3 in range(6)]
            for v8 in range(6):
                v9 = (v6 - v5[v8] + v1) % v1
                v7[v8][0] = v9
                for v10 in range(1, a2[v8]):
                    v7[v8][v10] = v2[v8][v10 - 1]
            v2 = v7
        return sum((sum(row) for v11 in v2)) % v1
