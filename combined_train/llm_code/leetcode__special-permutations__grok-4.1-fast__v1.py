class C1:

    def specialPerm(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = 1 << v2
        v4 = [[0] * v2 for v5 in range(v3)]
        for v6 in range(v2):
            v4[1 << v6][v6] = 1
        for v7 in range(v3):
            for v8 in range(v2):
                if v4[v7][v8] == 0:
                    continue
                for v9 in range(v2):
                    if v7 & 1 << v9:
                        continue
                    v10, v11 = (a1[v8], a1[v9])
                    if v10 % v11 == 0 or v11 % v10 == 0:
                        v4[v7 | 1 << v9][v9] = (v4[v7 | 1 << v9][v9] + v4[v7][v8]) % v1
        v12 = (1 << v2) - 1
        return sum(v4[v12]) % v1 if v2 else 1
