class C1(object):

    def maximumMedianSum(self, a1):
        """
        """
        a1.sort()
        return sum((a1[i] for v1 in range(len(a1) // 3, len(a1), 2)))
