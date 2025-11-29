class C1(object):

    def countDays(self, a1, a2):
        """
        """
        a2.sort()
        v1 = v2 = 0
        for v3, v4 in a2:
            v1 += max(v3 - 1 - v2, 0)
            v2 = max(v2, v4)
        v1 += a1 - v2
        return v1
