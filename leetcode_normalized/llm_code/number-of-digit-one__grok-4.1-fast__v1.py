class C1:

    def countDigitOne(self, a1):
        v1 = 0
        v2 = 1
        while v2 <= a1:
            v3 = v2 * 10
            v4 = a1 // v3
            v5 = a1 % v2
            v6 = a1 // v2 % 10
            v1 += v4 * v2
            if v6 > 1:
                v1 += v2
            elif v6 == 1:
                v1 += v5 + 1
            v2 *= 10
        return v1
