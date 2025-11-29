class C1(object):

    def maxProduct(self, a1):
        """
        """
        v1 = max(a1).bit_length()
        v2 = [0] * (1 << v1)
        for v3 in a1:
            v2[v3] = v3
        for v4 in range(v1):
            for v5 in range(1 << v1):
                if v5 & 1 << v4:
                    continue
                if v2[v5] > v2[v5 | 1 << v4]:
                    v2[v5 | 1 << v4] = v2[v5]
        v6 = 0
        for v3 in a1:
            if v3 * v2[(1 << v1) - 1 ^ v3] > v6:
                v6 = v3 * v2[(1 << v1) - 1 ^ v3]
        return v6
