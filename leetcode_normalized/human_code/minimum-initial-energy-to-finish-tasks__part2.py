class C1(object):

    def minimumEffort(self, a1):
        """
        """
        a1.sort(key=lambda x: x[0] - x[1])
        v1 = v2 = 0
        for v3, v4 in a1:
            v1 += max(v4 - v2, 0)
            v2 = max(v2, v4) - v3
        return v1
