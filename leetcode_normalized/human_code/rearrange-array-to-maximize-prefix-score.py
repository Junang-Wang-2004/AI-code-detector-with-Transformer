class C1(object):

    def maxScore(self, a1):
        """
        """
        a1.sort(reverse=True)
        v1 = 0
        for v2, v3 in enumerate(a1):
            v1 += v3
            if v1 <= 0:
                return v2
        return len(a1)
