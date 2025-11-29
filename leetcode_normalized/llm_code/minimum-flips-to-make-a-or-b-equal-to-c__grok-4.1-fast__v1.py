class C1:

    def minFlips(self, a1, a2, a3):
        v1 = 0
        for v2 in range(32):
            v3 = a1 >> v2 & 1
            v4 = a2 >> v2 & 1
            v5 = a3 >> v2 & 1
            if v5 == 0:
                v1 += v3 + v4
            elif v3 == 0 and v4 == 0:
                v1 += 1
        return v1
