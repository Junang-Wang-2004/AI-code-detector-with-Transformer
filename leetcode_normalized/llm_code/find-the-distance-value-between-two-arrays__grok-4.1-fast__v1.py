import bisect

class C1:

    def findTheDistanceValue(self, a1, a2, a3):
        v1 = sorted(a2)
        v2 = 0
        for v3 in a1:
            v4 = bisect.bisect_left(v1, v3 - a3)
            v5 = bisect.bisect_right(v1, v3 + a3)
            if v4 == v5:
                v2 += 1
        return v2
