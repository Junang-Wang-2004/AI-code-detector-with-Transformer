class C1:

    def atMostNGivenDigitSet(self, a1, a2):
        v1 = str(a2)
        v2 = len(v1)
        v3 = len(a1)
        v4 = set(a1)
        v5 = 0
        v6 = 1
        for v7 in range(v2 - 1):
            v6 *= v3
            v5 += v6
        v8 = v5
        v9 = v2
        v10 = True
        for v11 in range(v2):
            v12 = v1[v11]
            v13 = 0
            for v14 in a1:
                if v14 < v12:
                    v13 += 1
            v8 += v13 * v3 ** (v9 - 1)
            if v12 not in v4:
                v10 = False
                break
            v9 -= 1
        if v10:
            v8 += 1
        return v8
