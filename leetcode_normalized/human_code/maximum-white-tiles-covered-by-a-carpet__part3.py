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
        for v6, (v3, v7) in enumerate(a1):
            v4 = v3 + a2 - 1
            v8 = bisect.bisect_right(a1, [v4 + 1]) - 1
            v9 = max(a1[v8][1] - v4, 0)
            v5 = max(v5, v1[v8 + 1] - v1[v6] - v9)
        return v5
