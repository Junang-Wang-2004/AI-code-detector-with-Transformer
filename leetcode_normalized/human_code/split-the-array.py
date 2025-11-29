import collections

class C1(object):

    def isPossibleToSplit(self, a1):
        """
        """
        return all((v <= 2 for v1 in collections.Counter(a1).values()))
