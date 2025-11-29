from functools import reduce

class C1(object):

    def minMaxSums(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        a1.sort()
        v2 = 0
        v3 = 1
        for v4 in range(len(a1)):
            v3 = reduce(lambda accu, x: (accu + x) % v1, (nCr(v4, j) for v5 in range(min(v4, a2 - 1) + 1)), 0)
            v2 = (v2 + (a1[v4] + a1[~v4]) * v3) % v1
        return v2
