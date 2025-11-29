import collections

class C1(object):

    def stoneGameIX(self, a1):
        """
        """
        v1 = collections.Counter((x % 3 for v2 in a1))
        if v1[0] % 2 == 0:
            return v1[1] and v1[2]
        return abs(v1[1] - v1[2]) >= 3
