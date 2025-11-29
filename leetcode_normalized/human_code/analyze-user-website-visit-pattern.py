import collections
import itertools

class C1(object):

    def mostVisitedPattern(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(list)
        v2 = list(zip(a2, a1, a3))
        v2.sort()
        for v3, v4, v5 in v2:
            v1[v4].append(v5)
        v6 = sum([collections.Counter(set(itertools.combinations(v1[v4], 3))) for v4 in v1], collections.Counter())
        return list(min(v6, key=lambda x: (-v6[x], x)))
