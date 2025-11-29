class C1(object):

    def reverseBits(self, a1):
        v1 = 0
        for v2 in range(32):
            v1 <<= 1
            v1 |= a1 & 1
            a1 >>= 1
        return v1
