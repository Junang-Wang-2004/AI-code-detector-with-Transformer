class C1(object):

    def maxDistance(self, a1):
        """
        """
        for v1 in range(len(a1) // 2 + 1):
            if a1[~v1] != a1[0] or a1[v1] != a1[-1]:
                return len(a1) - v1
        return 0
