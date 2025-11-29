class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = sum((int(c) == i % 2 for v2, v3 in enumerate(a1)))
        return min(v1, len(a1) - v1)
