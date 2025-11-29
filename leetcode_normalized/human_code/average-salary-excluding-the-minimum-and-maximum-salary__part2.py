class C1(object):

    def average(self, a1):
        """
        """
        return 1.0 * (sum(a1) - min(a1) - max(a1)) / (len(a1) - 2)
