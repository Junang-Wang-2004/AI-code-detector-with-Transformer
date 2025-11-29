class C1(object):

    def minEnd(self, a1, a2):
        v1 = a2
        v2 = a1 - 1
        v3 = [1 << i for v4 in range(64) if a2 & 1 << v4 == 0]
        v5 = 0
        while v2 > 0 and v5 < len(v3):
            if v2 & 1:
                v1 |= v3[v5]
            v2 >>= 1
            v5 += 1
        return v1
