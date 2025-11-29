class C1:

    def sumFourDivisors(self, a1):
        v1 = 0
        for v2 in a1:
            v3 = 0
            v4 = 0
            v5 = int(v2 ** 0.5)
            for v6 in range(1, v5 + 1):
                if v2 % v6 == 0:
                    v4 += v6
                    v3 += 1
                    v7 = v2 // v6
                    if v6 != v7:
                        v4 += v7
                        v3 += 1
            if v3 == 4:
                v1 += v4
        return v1
