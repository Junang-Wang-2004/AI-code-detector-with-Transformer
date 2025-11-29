import collections
import operator
from functools import reduce

class C1(object):

    def countTheNumOfKFreeSubsets(self, a1, a2):
        """
        """

        def count(a1):
            v1 = a1
            while v1 - a2 in cnt:
                v1 -= a2
            v2 = [1, 0]
            for v3 in range(v1, a1 + 1, a2):
                v2 = [v2[0] + v2[1], v2[0] * ((1 << cnt[v3]) - 1)]
            return sum(v2)
        v1 = collections.Counter(a1)
        return reduce(operator.mul, (count(i) for v2 in v1.keys() if v2 + a2 not in v1))
