from functools import reduce

class C1(object):

    def longestSubsequence(self, a1):
        """
        """
        return len(a1) - int(reduce(lambda accu, x: accu ^ v1, a1, 0) == 0) if any((x for v1 in a1)) else 0
