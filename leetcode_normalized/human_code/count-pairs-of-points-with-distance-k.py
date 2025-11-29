import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        for v3, v4 in a1:
            for v5 in range(a2 + 1):
                v1 += v2.get((v3 ^ v5, v4 ^ a2 - v5), 0)
            v2[v3, v4] += 1
        return v1
