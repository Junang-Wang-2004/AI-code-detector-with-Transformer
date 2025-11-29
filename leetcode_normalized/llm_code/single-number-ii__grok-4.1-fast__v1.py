class C1:

    def singleNumber(self, a1):
        v1 = 0
        for v2 in range(32):
            v3 = sum((n >> v2 & 1 for v4 in a1)) % 3
            if v3 == 1:
                v1 |= 1 << v2
        return v1
