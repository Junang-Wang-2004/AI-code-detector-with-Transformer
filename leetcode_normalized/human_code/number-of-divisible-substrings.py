import collections

class C1(object):

    def countDivisibleSubstrings(self, a1):
        """
        """
        v1 = 0
        for v2 in range(1, 10):
            v3 = 0
            v4 = collections.Counter([0 + v2 * (-1 + 1)])
            for v5, v6 in enumerate(a1):
                v3 += (ord(v6) - ord('a') + 1) // 3 + 1
                v1 += v4[v3 - v2 * (v5 + 1)]
                v4[v3 - v2 * (v5 + 1)] += 1
        return v1
