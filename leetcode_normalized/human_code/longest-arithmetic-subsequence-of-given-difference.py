import collections

class C1(object):

    def longestSubsequence(self, a1, a2):
        """
        """
        v1 = 1
        v2 = collections.defaultdict(int)
        for v3 in range(len(a1)):
            v2[a1[v3]] = v2[a1[v3] - a2] + 1
            v1 = max(v1, v2[a1[v3]])
        return v1
