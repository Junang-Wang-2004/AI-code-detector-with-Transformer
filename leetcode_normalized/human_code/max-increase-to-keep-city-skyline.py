import itertools

class C1(object):

    def maxIncreaseKeepingSkyline(self, a1):
        """
        """
        v1 = [max(row) for v2 in a1]
        v3 = [max(col) for v4 in zip(*a1)]
        return sum((min(v1[r], v3[c]) - val for v5, v2 in enumerate(a1) for v6, v7 in enumerate(v2)))
