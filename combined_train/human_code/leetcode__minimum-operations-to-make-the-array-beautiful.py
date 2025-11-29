class C1(object):

    def minOperations(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = float('inf')
        v2 = max(a1)
        if v2 == 1:
            return 0
        v3 = [v1] * (2 * v2 - 2 + 1)
        v3[a1[0]] = 0
        for v4 in range(1, len(a1)):
            v5 = [v1] * len(v3)
            for v6 in range(1, len(v3)):
                if v3[v6] == v1:
                    continue
                for v7 in range(ceil_divide(a1[v4], v6), (len(v3) - 1) // v6 + 1):
                    v5[v7 * v6] = min(v5[v7 * v6], v3[v6] + (v7 * v6 - a1[v4]))
            v3 = v5
        return min(v3)
