from functools import reduce

class C1(object):

    def minCostII(self, a1):
        """
        """
        return min(reduce(self.combine, a1)) if a1 else 0

    def combine(self, a1, a2):
        v1, v2, v3 = (min(a1), len(a1), a1.index(min(a1)))
        a1, a1[v3] = ([v1] * v2, min(a1[:v3] + a1[v3 + 1:]))
        return list(map(sum, list(zip(a1, a2))))
