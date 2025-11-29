class C1:

    def reverseBits(self, a1):
        v1 = 0
        for v2 in range(32):
            if a1 & 1 << v2:
                v1 |= 1 << 31 - v2
        return v1
