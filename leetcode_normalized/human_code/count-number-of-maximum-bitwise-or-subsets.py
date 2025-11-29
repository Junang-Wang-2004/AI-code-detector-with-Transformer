import collections
from functools import reduce

class C1(object):

    def countMaxOrSubsets(self, a1):
        """
        """
        v1 = collections.Counter([0])
        for v2 in a1:
            for v3, v4 in list(v1.items()):
                v1[v3 | v2] += v4
        return v1[reduce(lambda x, y: v2 | y, a1)]
