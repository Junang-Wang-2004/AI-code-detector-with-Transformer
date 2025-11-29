import collections

class C1(object):

    def checkAlmostEquivalent(self, a1, a2):
        """
        """
        v1 = 3
        v2, v3 = (collections.Counter(a1), collections.Counter(a2))
        return all((abs(v2[c] - v3[c]) <= v1 for v4 in set(list(v2.keys()) + list(v3.keys()))))
