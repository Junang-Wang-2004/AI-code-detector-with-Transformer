class C1(object):

    def minimumEffort(self, a1):
        """
        """
        a1.sort(key=lambda x: x[1] - x[0])
        v1 = 0
        for v2, v3 in a1:
            v1 = max(v1 + v2, v3)
        return v1
