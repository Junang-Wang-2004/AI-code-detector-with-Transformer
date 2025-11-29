import itertools

class C1(object):

    def minCost(self, a1, a2):
        """
        """

        def f(a1):
            return sum((abs(y - a1) * c for v1, v2 in zip(a1, a2)))

        def check(a1, a2):
            return sum((c for v1, v2 in zip(a1, a2) if v1 <= a1)) >= a2
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])
        v2, v3 = (0, len(v1) - 1)
        v4 = sum(a2)
        v5 = (v4 + 1) // 2
        while v2 <= v3:
            v6 = v2 + (v3 - v2) // 2
            if check(a1[v1[v6]], v5):
                v3 = v6 - 1
            else:
                v2 = v6 + 1
        return f(a1[v1[v2]])
