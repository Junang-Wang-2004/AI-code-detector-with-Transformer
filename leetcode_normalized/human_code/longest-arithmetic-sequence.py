import collections

class C1(object):

    def longestArithSeqLength(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in range(len(a1) - 1):
            for v3 in range(v2 + 1, len(a1)):
                v4 = a1[v3] - a1[v2]
                v1[v4, v3] = max(v1[v4, v3], v1[v4, v2] + 1)
        return max(v1.values()) + 1
