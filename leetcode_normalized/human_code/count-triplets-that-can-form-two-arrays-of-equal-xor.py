import collections

class C1(object):

    def countTriplets(self, a1):
        """
        """
        v1 = collections.defaultdict(lambda: [0, 0])
        v1[0] = [1, 0]
        v2, v3 = (0, 0)
        for v4, v5 in enumerate(a1):
            v3 ^= v5
            v6, v7 = v1[v3]
            v2 += v6 * v4 - v7
            v1[v3] = [v6 + 1, v7 + v4 + 1]
        return v2
