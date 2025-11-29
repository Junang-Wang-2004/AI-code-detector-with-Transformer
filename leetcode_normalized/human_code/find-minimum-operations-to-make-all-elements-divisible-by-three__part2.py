class C1(object):

    def minimumOperations(self, a1):
        """
        """
        return sum((min(x % 3, 3 - x % 3) for v1 in a1))
