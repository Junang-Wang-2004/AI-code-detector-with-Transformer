import itertools

class C1(object):

    def minCost(self, a1, a2, a3):
        """
        """

        def cost():
            return sum((abs(x - y) for v1, v2 in zip(a1, a2)))
        v1 = cost()
        a1.sort()
        a2.sort()
        v1 = min(v1, a3 + cost())
        return v1
