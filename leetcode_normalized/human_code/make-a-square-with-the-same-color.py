import collections

class C1(object):

    def canMakeSquare(self, a1):
        """
        """
        v1, v2 = (3, 2)
        return any((max(collections.Counter((a1[i + h][j + w] for v3 in range(v2) for v4 in range(v2))).values()) >= v2 ** 2 - 1 for v5 in range(v1 - v2 + 1) for v6 in range(v1 - v2 + 1)))
