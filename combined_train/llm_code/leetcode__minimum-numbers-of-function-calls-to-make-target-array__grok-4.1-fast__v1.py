class C1(object):

    def minOperations(self, a1):
        v1 = 0
        for v2 in a1:
            v3 = 0
            v4 = v2
            while v4:
                v3 += 1
                v4 >>= 1
            if v3 > v1:
                v1 = v3
        v5 = 0
        for v2 in a1:
            v3 = 0
            v4 = v2
            while v4:
                if v4 & 1:
                    v3 += 1
                v4 >>= 1
            v5 += v3
        return v5 + max(0, v1 - 1)
