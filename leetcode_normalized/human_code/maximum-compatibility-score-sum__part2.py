class C1(object):

    def maxCompatibilitySum(self, a1, a2):
        """
        """

        def popcount(a1):
            v1 = 0
            while a1:
                a1 &= a1 - 1
                v1 += 1
            return v1

        def masks(a1):
            v1 = []
            for v2 in a1:
                v3, v4 = (0, 1)
                for v5 in range(len(v2)):
                    if v2[v5]:
                        v3 |= v4
                    v4 <<= 1
                v1.append(v3)
            return v1
        v1, v2 = (masks(a1), masks(a2))
        v3 = [(0, 0)] * 2 ** len(v2)
        for v4 in range(len(v3)):
            v5 = 1
            for v6 in range(len(v2)):
                if v4 & v5 == 0:
                    v3[v4 | v5] = max(v3[v4 | v5], (v3[v4][0] + (len(a1[0]) - popcount(v1[v3[v4][1]] ^ v2[v6])), v3[v4][1] + 1))
                v5 <<= 1
        return v3[-1][0]
