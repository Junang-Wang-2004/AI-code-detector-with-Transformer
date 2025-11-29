import itertools

class C1(object):

    def gridGame(self, a1):
        """
        """
        v1 = float('inf')
        v2, v3 = (0, sum(a1[0]))
        for v4, v5 in zip(a1[0], a1[1]):
            v3 -= v4
            v1 = min(v1, max(v2, v3))
            v2 += v5
        return v1
