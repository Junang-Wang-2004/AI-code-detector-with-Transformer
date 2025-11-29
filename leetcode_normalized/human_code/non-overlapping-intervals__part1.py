class C1(object):

    def eraseOverlapIntervals(self, a1):
        """
        """
        a1.sort(key=lambda interval: interval[1])
        v1, v2 = (0, float('-inf'))
        for v3, v4 in a1:
            if v3 < v2:
                v1 += 1
            else:
                v2 = v4
        return v1
