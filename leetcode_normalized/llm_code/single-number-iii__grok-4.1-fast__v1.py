class C1:

    def singleNumber(self, a1):
        v1 = 0
        for v2 in a1:
            v1 ^= v2
        v3 = 1
        while v1 & v3 == 0:
            v3 <<= 1
        v4 = 0
        v5 = 0
        for v2 in a1:
            if v2 & v3:
                v4 ^= v2
            else:
                v5 ^= v2
        return [v4, v5]
