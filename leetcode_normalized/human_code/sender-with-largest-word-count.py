import collections
import itertools

class C1(object):

    def largestWordCount(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        for v2, v3 in zip(a1, a2):
            v1[v3] += v2.count(' ') + 1
        return max((k for v4 in v1.keys()), key=lambda x: (v1[x], x))
