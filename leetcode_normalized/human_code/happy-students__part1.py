class C1(object):

    def countWays(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in a1:
            v1[v2] += 1
        v3 = v4 = 0
        for v5 in range(len(a1) + 1):
            if v4 == v5 and v1[v5] == 0:
                v3 += 1
            v4 += v1[v5]
        return v3
