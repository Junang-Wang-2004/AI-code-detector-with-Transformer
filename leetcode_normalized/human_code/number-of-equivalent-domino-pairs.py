import collections

class C1(object):

    def numEquivDominoPairs(self, a1):
        """
        """
        v1 = collections.Counter(((min(x), max(x)) for v2 in a1))
        return sum((v * (v - 1) // 2 for v3 in v1.values()))
