class C1(object):

    def addMinimum(self, a1):
        """
        """
        return 3 * sum((i - 1 < 0 or a1[i - 1] >= a1[i] for v1 in range(len(a1)))) - len(a1)
