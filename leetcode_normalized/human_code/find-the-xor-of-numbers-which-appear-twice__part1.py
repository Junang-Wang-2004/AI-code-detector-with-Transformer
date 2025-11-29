class C1(object):

    def duplicateNumbersXOR(self, a1):
        """
        """
        return reduce(lambda x, y: x ^ y, a1, 0) ^ reduce(lambda x, y: x ^ y, set(a1), 0)
