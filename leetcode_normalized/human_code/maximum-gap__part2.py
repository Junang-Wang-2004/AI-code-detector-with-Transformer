class C1(object):

    def maximumGap(self, a1):
        """
        """
        if len(a1) < 2:
            return 0
        a1.sort()
        v1 = a1[0]
        v2 = float('-inf')
        for v3 in a1:
            v2 = max(v2, v3 - v1)
            v1 = v3
        return v2
