class C1(object):

    def waysToReachStair(self, a1):
        """
        """

        def ceil_log2_x(a1):
            return (a1 - 1).bit_length()
        v1 = ceil_log2_x(a1)
        while (1 << v1) - a1 <= v1 + 1:
            v1 += 1
        v2 = [1] * (v1 + 1)
        for v3 in range(len(v2) - 1):
            v2[v3 + 1] = v2[v3] * (v3 + 1)

        def nCr(a1, a2):
            if not 0 <= a2 <= a1:
                return 0
            return v2[a1] // v2[a2] // v2[a1 - a2]
        return sum((nCr(v3 + 1, (1 << v3) - a1) for v3 in range(v1)))
