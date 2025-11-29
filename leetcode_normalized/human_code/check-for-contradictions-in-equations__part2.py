import itertools

class C1(object):

    def checkContradictions(self, a1, a2):
        """
        """
        v1 = 1e-05
        v2 = UnionFind()
        return any((not v2.union_set(a, b, k) and abs(v2.query_set(a, b) - k) >= v1 for (v3, v4), v5 in zip(a1, a2)))
