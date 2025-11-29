import collections

class C1(object):

    def sumOfUnique(self, a1):
        """
        """
        return sum((x for v1, v2 in collections.Counter(a1).items() if v2 == 1))
