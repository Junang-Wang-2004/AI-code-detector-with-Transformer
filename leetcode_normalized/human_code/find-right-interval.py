import bisect

class C1(object):

    def findRightInterval(self, a1):
        """
        """
        v1 = sorted(((interval.start, i) for v2, v3 in enumerate(a1)))
        v4 = []
        for v3 in a1:
            v5 = bisect.bisect_left(v1, (v3.end,))
            v4.append(v1[v5][1] if v5 < len(v1) else -1)
        return v4
