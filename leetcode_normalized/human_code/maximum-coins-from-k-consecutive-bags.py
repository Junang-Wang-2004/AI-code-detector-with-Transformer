class C1(object):

    def maximumCoins(self, a1, a2):
        """
        """

        def max_amount():
            a1.sort()
            v1 = v2 = v3 = 0
            for v4 in range(len(a1)):
                v2 += (a1[v4][1] - a1[v4][0] + 1) * a1[v4][2]
                while a1[v4][1] - a1[v3][1] + 1 > a2:
                    v2 -= (a1[v3][1] - a1[v3][0] + 1) * a1[v3][2]
                    v3 += 1
                v1 = max(v1, v2 - max(a1[v4][1] - a1[v3][0] + 1 - a2, 0) * a1[v3][2])
            return v1
        v1 = max_amount()
        for v2, (v3, v4, v5) in enumerate(a1):
            a1[v2][:] = [-v4, -v3, v5]
        v1 = max(v1, max_amount())
        return v1
