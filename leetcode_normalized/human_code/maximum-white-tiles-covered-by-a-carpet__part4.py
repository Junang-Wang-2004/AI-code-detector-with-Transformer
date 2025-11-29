import bisect

class C1(object):

    def maximumWhiteTiles(self, a1, a2):
        """
        """
        a1.sort()
        v1 = [0] * (len(a1) + 1)
        for v2, (v3, v4) in enumerate(a1):
            v1[v2 + 1] = v1[v2] + (v4 - v3 + 1)
        v5 = 0
        for v6, (v7, v4) in enumerate(a1):
            v3 = v4 - a2 + 1
            v8 = bisect.bisect_right(a1, [v3])
            if v8 - 1 >= 0 and a1[v8 - 1][1] + 1 >= v3:
                v8 -= 1
            v9 = max(v3 - a1[v8][0], 0)
            v5 = max(v5, v1[v6 + 1] - v1[v8] - v9)
        return v5
