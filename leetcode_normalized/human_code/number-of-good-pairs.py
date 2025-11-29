import collections

class C1(object):

    def numIdenticalPairs(self, a1):
        """
        """
        return sum((c * (c - 1) // 2 for v1 in collections.Counter(a1).values()))
