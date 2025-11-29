from functools import reduce

class C1(object):

    def maximumRows(self, a1, a2):
        """
        """

        def next_popcount(a1):
            v1 = a1 & -a1
            v2 = a1 + v1
            v3 = a1 ^ v2
            v4 = v3 // v1 >> 2
            return v2 | v4
        v1 = [reduce(lambda m, c: m | a1[r][-1 - c] << c, range(len(a1[0])), 0) for v2 in range(len(a1))]
        v3 = 0
        v4 = (1 << a2) - 1
        while v4 < 1 << len(a1[0]):
            v3 = max(v3, sum((m & v4 == m for v5 in v1)))
            v4 = next_popcount(v4)
        return v3
