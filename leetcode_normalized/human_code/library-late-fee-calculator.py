class C1(object):

    def lateFee(self, a1):
        """
        """
        return sum((1 if i == 1 else 3 * i if i >= 6 else 2 * i for v1 in a1))
