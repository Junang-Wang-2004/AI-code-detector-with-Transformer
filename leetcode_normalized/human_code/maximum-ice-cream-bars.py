class C1(object):

    def maxIceCream(self, a1, a2):
        """
        """
        a1.sort()
        for v1, v2 in enumerate(a1):
            a2 -= v2
            if a2 < 0:
                return v1
        return len(a1)
