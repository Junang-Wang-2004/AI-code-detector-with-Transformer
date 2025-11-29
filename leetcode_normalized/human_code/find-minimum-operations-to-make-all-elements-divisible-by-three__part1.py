class C1(object):

    def minimumOperations(self, a1):
        """
        """
        return sum((x % 3 != 0 for v1 in a1))
