import itertools

class C1(object):

    def minNumberOfHours(self, a1, a2, a3, a4):
        """
        """
        v1 = 0
        for v2, v3 in zip(a3, a4):
            v4 = max(v2 + 1 - a1, 0)
            v5 = max(v3 + 1 - a2, 0)
            v1 += v4 + v5
            a1 += v4 - v2
            a2 += v5 + v3
        return v1
