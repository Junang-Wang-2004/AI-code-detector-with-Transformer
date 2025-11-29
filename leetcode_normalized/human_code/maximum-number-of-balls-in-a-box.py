import collections
import itertools

class C1(object):

    def countBalls(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        for v2 in range(a1, a2 + 1):
            v1[sum(map(int, str(v2)))] += 1
        return max(v1.values())
