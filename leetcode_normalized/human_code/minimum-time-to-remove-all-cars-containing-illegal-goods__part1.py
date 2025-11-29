class C1(object):

    def minimumTime(self, a1):
        """
        """
        v1 = 0
        v2 = v1 + (len(a1) - 0)
        for v3 in range(1, len(a1) + 1):
            v1 = min(v1 + 2 * (a1[v3 - 1] == '1'), v3)
            v2 = min(v2, v1 + (len(a1) - v3))
        return v2
