from functools import reduce

class C1(object):

    def stoneGameVIII(self, a1):
        """
        """
        for v1 in range(len(a1) - 1):
            a1[v1 + 1] += a1[v1]
        return reduce(lambda curr, i: max(curr, a1[v1] - curr), reversed(range(1, len(a1) - 1)), a1[-1])
