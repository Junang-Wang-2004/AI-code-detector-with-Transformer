class C1:

    def hammingDistance(self, a1, a2):
        v1 = 0
        for v2 in range(32):
            if a1 & 1 != a2 & 1:
                v1 += 1
            a1 >>= 1
            a2 >>= 1
        return v1
