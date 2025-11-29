class C1(object):

    def maximumPopulation(self, a1):
        """
        """
        v1, v2 = (1950, 2050)
        v3 = [0] * (v2 - v1 + 1)
        for v4, v5 in a1:
            v3[v4 - v1] += 1
            v3[v5 - v1] -= 1
        v6 = 0
        for v7 in range(len(v3)):
            if v7:
                v3[v7] += v3[v7 - 1]
            if v3[v7] > v3[v6]:
                v6 = v7
        return v6 + v1
