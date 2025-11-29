class C1(object):

    def maxAdjacentDistance(self, a1):
        """
        """
        return max((abs(a1[i] - a1[i - 1]) for v1 in range(len(a1))))
