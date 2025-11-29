class C1(object):

    def numberOfPairs(self, a1, a2, a3):
        """
        """
        return sum((x % (a3 * y) == 0 for v1 in a1 for v2 in a2))
