class C1(object):

    def perfectPairs(self, a1):
        """
        """
        for v1 in range(len(a1)):
            a1[v1] = abs(a1[v1])
        a1.sort()
        v2 = v3 = 0
        for v4 in range(len(a1)):
            while not a1[v4] - a1[v3] <= a1[v3]:
                v3 += 1
            v2 += v4 - v3 + 1 - 1
        return v2
