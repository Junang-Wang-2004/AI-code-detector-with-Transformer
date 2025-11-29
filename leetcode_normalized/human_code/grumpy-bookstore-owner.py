class C1(object):

    def maxSatisfied(self, a1, a2, a3):
        """
        """
        v1, v2, v3 = (0, 0, 0)
        for v4 in range(len(a1)):
            v1 += 0 if a2[v4] else a1[v4]
            v3 += a1[v4] if a2[v4] else 0
            if v4 >= a3:
                v3 -= a1[v4 - a3] if a2[v4 - a3] else 0
            v2 = max(v2, v3)
        return v1 + v2
