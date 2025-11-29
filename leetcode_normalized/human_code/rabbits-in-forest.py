import collections

class C1(object):

    def numRabbits(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        return sum(((k + 1 + v - 1) // (k + 1) * (k + 1) for v2, v3 in v1.items()))
