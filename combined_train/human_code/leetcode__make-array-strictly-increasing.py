import collections
import bisect

class C1(object):

    def makeArrayIncreasing(self, a1, a2):
        """
        """
        a2 = sorted(set(a2))
        v2 = {0: -1}
        for v3 in a1:
            v4 = collections.defaultdict(lambda: float('inf'))
            for v5, v6 in v2.items():
                if v6 < v3:
                    v4[v5] = min(v4[v5], v3)
                v7 = bisect.bisect_right(a2, v6)
                if v7 == len(a2):
                    continue
                v4[v5 + 1] = min(v4[v5 + 1], a2[v7])
            v2 = v4
            if not v2:
                return -1
        return min(v2.keys())
