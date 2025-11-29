class C1(object):

    def maxProduct(self, a1):
        """
        """
        v1 = max(a1).bit_length()
        v2 = [0] * (1 << v1)
        for v3 in a1:
            v2[v3] = v3
        for v4 in range(v1):
            for v5 in range(0, 1 << v1, 1 << v4 + 1):
                for v6 in range(v5, v5 + (1 << v4)):
                    if v2[v6] > v2[v6 + (1 << v4)]:
                        v2[v6 + (1 << v4)] = v2[v6]
        v7 = 0
        for v3 in a1:
            if v3 * v2[(1 << v1) - 1 ^ v3] > v7:
                v7 = v3 * v2[(1 << v1) - 1 ^ v3]
        return v7
