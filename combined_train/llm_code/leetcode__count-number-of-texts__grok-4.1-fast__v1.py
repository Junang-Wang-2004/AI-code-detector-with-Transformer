class C1:

    def countTexts(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 1
        v3 = len(a1)
        v4 = 0
        while v4 < v3:
            v5 = v4
            v6 = a1[v4]
            while v4 < v3 and a1[v4] == v6:
                v4 += 1
            v7 = v4 - v5
            v8 = 4 if v6 in '79' else 3
            v9 = [0] * (v7 + 1)
            v9[0] = 1
            for v10 in range(1, v7 + 1):
                for v11 in range(1, min(v8, v10) + 1):
                    v9[v10] = (v9[v10] + v9[v10 - v11]) % v1
            v2 = v2 * v9[v7] % v1
        return v2
