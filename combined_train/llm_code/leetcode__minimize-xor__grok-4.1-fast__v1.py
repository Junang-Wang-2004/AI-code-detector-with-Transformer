class C1(object):

    def minimizeXor(self, a1, a2):
        v1 = 0
        v2 = a2
        while v2:
            v1 += v2 & 1
            v2 >>= 1
        v3 = 0
        v4 = 0
        for v5 in range(60, -1, -1):
            v6 = a1 >> v5 & 1
            v7 = v1 - v4 - v6
            v8 = v5
            if 0 <= v7 <= v8:
                v9 = v6
            else:
                v9 = 1 ^ v6
            v3 |= v9 << v5
            v4 += v9
        return v3
