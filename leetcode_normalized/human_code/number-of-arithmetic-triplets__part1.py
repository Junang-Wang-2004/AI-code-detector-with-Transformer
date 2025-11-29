class C1(object):

    def arithmeticTriplets(self, a1, a2):
        """
        """
        v1 = set(a1)
        return sum((x - a2 in v1 and x - 2 * a2 in v1 for v2 in a1))
