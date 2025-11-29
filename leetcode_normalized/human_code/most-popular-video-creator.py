import collections
import itertools

class C1(object):

    def mostPopularCreator(self, a1, a2, a3):
        """
        """
        v1 = collections.Counter()
        v2 = collections.defaultdict(lambda: (float('inf'), float('inf')))
        for v3, v4, v5 in zip(a1, a2, a3):
            v1[v3] += v5
            v2[v3] = min(v2[v3], (-v5, v4))
        v6 = max(v1.values())
        return [[k, v2[k][1]] for v7, v5 in v1.items() if v5 == v6]
