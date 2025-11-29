class C1(object):

    def findMinDifference(self, a1):
        """
        """
        v1 = [int(x[:2]) * 60 + int(x[3:]) for v2 in a1]
        v1.sort()
        return min(((y - v2) % (24 * 60) for v2, v3 in zip(v1, v1[1:] + v1[:1])))
