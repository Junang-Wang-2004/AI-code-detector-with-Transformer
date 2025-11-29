class C1(object):

    def maximumBobPoints(self, a1, a2):
        """
        """

        def check(a1, a2):
            v1 = 0
            v2 = [0] * len(a2)
            v3, v4 = (0, 1)
            for v5, v6 in enumerate(a2):
                if a1 & 1:
                    v7 = v6 + 1
                    if v7 > a2:
                        return (0, [0] * len(a2))
                    a2 -= v7
                    v2[v5] = v7
                    v1 += v5
                a1 >>= 1
            v2[-1] += a2
            return (v1, v2)
        v1 = [0] * len(a2)
        v2 = 0
        for v3 in range(1, 2 ** len(a2)):
            v4, v5 = check(v3, a1)
            if v4 > v2:
                v2 = v4
                v1 = v5
        return v1
