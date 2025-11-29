class C1(object):

    def findNonMinOrMax(self, a1):
        """
        """
        v1, v2 = (float('-inf'), float('inf'))
        v3 = -1
        for v4 in a1:
            if v2 < v4 < v1:
                return v4
            if v4 < v2:
                v3 = v2
                v2 = v4
            if v4 > v1:
                v3 = v1
                v1 = v4
        return v3 if v2 < v3 < v1 else -1
