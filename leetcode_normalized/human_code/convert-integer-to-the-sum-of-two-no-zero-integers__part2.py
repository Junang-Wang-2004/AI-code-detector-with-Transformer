class C1(object):

    def getNoZeroIntegers(self, a1):
        """
        """
        return next(([a, a1 - a] for v1 in range(1, a1) if '0' not in '{}{}'.format(v1, a1 - v1)))
