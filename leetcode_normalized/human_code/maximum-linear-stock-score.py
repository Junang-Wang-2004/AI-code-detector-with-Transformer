import collections

class C1(object):

    def maxScore(self, a1):
        """
        """
        v1 = collections.Counter()
        for v2, v3 in enumerate(a1):
            v1[v3 - v2] += v3
        return max(v1.values())
