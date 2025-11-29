class C1:

    def countPrimeSetBits(self, a1, a2):
        v1 = {2, 3, 5, 7, 11, 13, 17, 19}
        v2 = 0
        for v3 in range(a1, a2 + 1):
            v4 = bin(v3).count('1')
            if v4 in v1:
                v2 += 1
        return v2
