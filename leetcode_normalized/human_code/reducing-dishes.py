class C1(object):

    def maxSatisfaction(self, a1):
        """
        """
        a1.sort(reverse=True)
        v1, v2 = (0, 0)
        for v3 in a1:
            v2 += v3
            if v2 <= 0:
                break
            v1 += v2
        return v1
