import itertools

class C1(object):

    def minCost(self, a1, a2):
        """
        """

        def f(a1):
            return sum((abs(y - a1) * c for v1, v2 in zip(a1, a2)))

        def check(a1):
            return a1 + 1 == len(idxs) or f(a1[idxs[a1]]) < f(a1[idxs[a1 + 1]])
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])
        v2, v3 = (0, len(v1) - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if check(v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return f(a1[v1[v2]])
