class C1(object):

    def largestPerimeter(self, a1):
        """
        """
        a1.sort()
        for v1 in reversed(range(len(a1) - 2)):
            if a1[v1] + a1[v1 + 1] > a1[v1 + 2]:
                return a1[v1] + a1[v1 + 1] + a1[v1 + 2]
        return 0
