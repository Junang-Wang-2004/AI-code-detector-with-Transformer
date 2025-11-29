class C1:

    def minimumFinishTime(self, a1, a2, a3):
        v1 = 10 ** 18
        v2 = (a2 + 1).bit_length() + 5
        v3 = [v1] * v2
        for v4, v5 in a1:
            v6 = 0
            v7 = v4
            v8 = 0
            while v7 < a2 + v4 and v8 < v2:
                v6 += v7
                v3[v8] = min(v3[v8], v6)
                v7 *= v5
                v8 += 1
        v9 = [v1] * (a3 + 1)
        v9[0] = 0
        for v10 in range(1, a3 + 1):
            for v11 in range(1, min(v10, v2) + 1):
                v12 = v3[v11 - 1]
                if v12 == v1:
                    continue
                v13 = v10 - v11
                v14 = a2 if v13 > 0 else 0
                v9[v10] = min(v9[v10], v9[v13] + v14 + v12)
        return v9[a3]
