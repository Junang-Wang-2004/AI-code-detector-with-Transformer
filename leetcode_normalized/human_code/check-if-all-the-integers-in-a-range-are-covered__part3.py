class C1(object):

    def isCovered(self, a1, a2, a3):
        """
        """
        return all((any((l <= i <= r for v1, v2 in a1)) for v3 in range(a2, a3 + 1)))
