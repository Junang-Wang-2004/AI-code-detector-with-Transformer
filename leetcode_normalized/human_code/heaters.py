import bisect

class C1(object):

    def findRadius(self, a1, a2):
        """
        """
        a2.sort()
        v1 = 0
        for v2 in a1:
            v3 = bisect.bisect_left(a2, v2)
            v4 = float('inf')
            if v3 != len(a2):
                v4 = a2[v3] - v2
            if v3 != 0:
                v5 = v3 - 1
                v4 = min(v4, v2 - a2[v5])
            v1 = max(v1, v4)
        return v1
