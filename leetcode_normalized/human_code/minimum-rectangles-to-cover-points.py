class C1(object):

    def minRectanglesToCoverPoints(self, a1, a2):
        """
        """
        a1.sort(key=lambda x: x[0])
        v1 = 0
        v2 = -(a2 + 1)
        for v3, v4 in a1:
            if v3 - v2 <= a2:
                continue
            v2 = v3
            v1 += 1
        return v1
