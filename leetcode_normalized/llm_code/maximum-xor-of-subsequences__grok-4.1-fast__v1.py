class C1(object):

    def maxXorSubsequences(self, a1):
        if not a1:
            return 0
        v1 = max((n.bit_length() for v2 in a1))
        v3 = [0] * v1
        for v4 in a1:
            v5 = v4
            for v6 in range(v1 - 1, -1, -1):
                if v3[v6] and v5 & 1 << v6:
                    v5 ^= v3[v6]
            if v5:
                v7 = v5.bit_length() - 1
                v3[v7] = v5
        v8 = 0
        for v6 in range(v1 - 1, -1, -1):
            if v8 ^ v3[v6] > v8:
                v8 ^= v3[v6]
        return v8
