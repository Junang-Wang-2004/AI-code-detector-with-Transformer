import collections
import itertools
import heapq

class C1(object):

    def maxProbability(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = collections.defaultdict(list)
        for (v2, v3), v4 in zip(a2, a3):
            v1[v2].append((v3, v4))
            v1[v3].append((v2, v4))
        v5 = [(-1.0, a4)]
        v6, v7 = (collections.defaultdict(float), set())
        v6[a4] = 1.0
        while v5 and len(v7) != len(v1):
            v8, v2 = heapq.heappop(v5)
            if v2 in v7:
                continue
            v7.add(v2)
            for v3, v9 in v1[v2]:
                if v3 in v7:
                    continue
                if v3 in v6 and v6[v3] >= -v8 * v9:
                    continue
                v6[v3] = -v8 * v9
                heapq.heappush(v5, (-v6[v3], v3))
        return v6[a5]
