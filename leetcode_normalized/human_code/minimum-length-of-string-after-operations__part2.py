import collections

class C1(object):

    def minimumLength(self, a1):
        """
        """
        return sum((2 - x % 2 for v1 in collections.Counter(a1).values()))
