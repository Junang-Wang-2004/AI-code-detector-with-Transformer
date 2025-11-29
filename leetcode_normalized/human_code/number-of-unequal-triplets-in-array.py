import collections

class C1(object):

    def unequalTriplets(self, a1):
        """
        """
        v1 = 3
        v2 = collections.Counter()
        v3 = [0] * v1
        for v4 in a1:
            v2[v4] += 1
            v5 = 1
            for v6 in range(v1):
                v3[v6] += v5
                v5 = v3[v6] - v2[v4] * v5
        return v3[v1 - 1]
