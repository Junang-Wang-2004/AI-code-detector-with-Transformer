import collections

class C1(object):

    def minOperations(self, a1):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = collections.Counter(a1)
        return sum((ceil_divide(v2, 3) for v2 in v1.values())) if all((x >= 2 for v2 in v1.values())) else -1
