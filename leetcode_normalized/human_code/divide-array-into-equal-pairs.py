import collections

class C1(object):

    def divideArray(self, a1):
        """
        """
        return all((cnt % 2 == 0 for v1 in collections.Counter(a1).values()))
