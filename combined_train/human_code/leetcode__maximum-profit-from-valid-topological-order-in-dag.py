class C1(object):

    def maxProfit(self, a1, a2, a3):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')
        v1 = [0] * a1
        for v2, v3 in a2:
            v1[v3] |= 1 << v2
        v4 = [-1] * (1 << a1)
        v4[0] = 0
        for v5 in range(1 << a1):
            if v4[v5] == -1:
                continue
            v6 = popcount(v5) + 1
            for v2 in range(a1):
                if v5 & 1 << v2:
                    continue
                if v5 & v1[v2] == v1[v2]:
                    v4[v5 | 1 << v2] = max(v4[v5 | 1 << v2], v4[v5] + v6 * a3[v2])
        return v4[-1]
