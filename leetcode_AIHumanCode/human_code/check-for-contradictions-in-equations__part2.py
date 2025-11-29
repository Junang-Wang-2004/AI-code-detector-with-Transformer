# Time:  O(e + q)
# Space: O(n)
import itertools


# union find
class Solution(object):
    def checkContradictions(self, equations, values):
        """
        """
        EPS = 1e-5
        uf = UnionFind()
        return any(not uf.union_set(a, b, k) and abs(uf.query_set(a, b)-k) >= EPS for (a, b), k in zip(equations, values))


