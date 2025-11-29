import collections
import itertools

class C1(object):

    def minimumTotalCost(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        v2 = 0
        for v3, (v4, v5) in enumerate(zip(a1, a2)):
            if v4 != v5:
                continue
            v1[v4] += 1
            v2 += v3
        if not v1:
            return 0
        v6 = max(iter(v1.keys()), key=lambda x: v1[v4])
        v7 = v1[v6] - (sum(v1.values()) - v1[v6])
        if v7 <= 0:
            return v2
        for v3, (v4, v5) in enumerate(zip(a1, a2)):
            if v4 == v5 or v6 in (v4, v5):
                continue
            v2 += v3
            v7 -= 1
            if not v7:
                return v2
        return -1
