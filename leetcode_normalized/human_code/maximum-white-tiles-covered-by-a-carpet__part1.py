class C1(object):

    def maximumWhiteTiles(self, a1, a2):
        """
        """
        a1.sort()
        v1 = v2 = v3 = 0
        for v4, (v5, v6) in enumerate(a1):
            if v4 - 1 >= 0:
                v3 -= a1[v4][0] - a1[v4 - 1][1] - 1
            v7 = v5 + a2 - 1
            while v2 + 1 < len(a1) and v7 + 1 >= a1[v2 + 1][0]:
                v2 += 1
                v3 += a1[v2][0] - a1[v2 - 1][1] - 1
            v1 = max(v1, min(a1[v2][1] - a1[v4][0] + 1, a2) - v3)
        return v1
