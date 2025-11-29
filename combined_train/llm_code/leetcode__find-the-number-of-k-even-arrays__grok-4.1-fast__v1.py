class C1:

    def countOfArrays(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = a2 // 2
        v3 = (a2 + 1) // 2
        v4 = [0] * (a3 + 1)
        v5 = [0] * (a3 + 1)
        v4[0] = v2
        v5[0] = v3
        for v6 in range(1, a1):
            v7 = [0] * (a3 + 1)
            v8 = [0] * (a3 + 1)
            for v9 in range(a3 + 1):
                v7[v9] = v4[v9] * v2 % v1
                if v9 > 0:
                    v7[v9] = (v7[v9] + v5[v9 - 1] * v2) % v1
                v8[v9] = v5[v9] * v3 % v1
                if v9 > 0:
                    v8[v9] = (v8[v9] + v4[v9 - 1] * v3) % v1
            v4 = v7
            v5 = v8
        return (v4[a3] + v5[a3]) % v1
