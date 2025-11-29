import collections

class C1(object):

    def countBadPairs(self, a1):
        """
        """
        v1 = len(a1) * (len(a1) - 1) // 2
        v2 = collections.Counter()
        for v3, v4 in enumerate(a1):
            v1 -= v2[v4 - v3]
            v2[v4 - v3] += 1
        return v1
