import bisect

class C1(object):

    def findTheDistanceValue(self, a1, a2, a3):
        """
        """
        a2.sort()
        v1, v2, v3 = (0, 0, 0)
        for v4 in a1:
            v3 = bisect.bisect_left(a2, v4)
            v5 = a2[v3 - 1] if v3 - 1 >= 0 else float('-inf')
            v6 = a2[v3] if v3 < len(a2) else float('inf')
            v1 += v5 + a3 < v4 < v6 - a3
        return v1
