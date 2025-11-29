class C1(object):

    def maxTotalReward(self, a1):
        v1 = max(a1)
        v2 = sorted((v for v3 in set(a1) if v3 < v1))
        v4 = (1 << v1) - 1
        v5 = 1
        for v6 in v2:
            v7 = v5 & (1 << v6) - 1
            v5 |= v7 << v6 & v4
        v8 = v5.bit_length() - 1
        return v1 + v8
