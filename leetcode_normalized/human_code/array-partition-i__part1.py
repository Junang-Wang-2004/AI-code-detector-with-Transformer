class C1(object):

    def arrayPairSum(self, a1):
        """
        """
        v1, v2 = (-10000, 10000)
        v3 = [0] * (v2 - v1 + 1)
        for v4 in a1:
            v3[v4 - v1] += 1
        v5, v6 = (0, 0)
        for v7 in range(v1, v2 + 1):
            v6 += (v3[v7 - v1] + 1 - v5) / 2 * v7
            v5 = (v3[v7 - v1] + v5) % 2
        return v6
