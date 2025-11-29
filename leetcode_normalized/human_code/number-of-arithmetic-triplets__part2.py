import collections

class C1(object):

    def arithmeticTriplets(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        v3 = collections.Counter()
        for v4 in a1:
            v1 += v3[v4 - a2]
            v3[v4] += v2[v4 - a2]
            v2[v4] += 1
        return v1
