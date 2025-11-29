class C1(object):

    def removeCoveredIntervals(self, a1):
        """
        """
        a1.sort(key=lambda x: [x[0], -x[1]])
        v1, v2 = (0, 0)
        for v3, v4 in a1:
            v1 += int(v4 > v2)
            v2 = max(v2, v4)
        return v1
