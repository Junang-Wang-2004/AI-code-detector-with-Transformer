import collections

class C1(object):

    def longestCommomSubsequence(self, a1):
        """
        """
        return [num for v1, v2 in collections.Counter((x for v3 in a1 for v4 in v3)).items() if v2 == len(a1)]
