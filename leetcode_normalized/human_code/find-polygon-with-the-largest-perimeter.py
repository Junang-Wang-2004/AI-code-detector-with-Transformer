class C1(object):

    def largestPerimeter(self, a1):
        """
        """
        a1.sort()
        v1 = sum(a1)
        for v2 in reversed(range(2, len(a1))):
            v1 -= a1[v2]
            if v1 > a1[v2]:
                return v1 + a1[v2]
        return -1
