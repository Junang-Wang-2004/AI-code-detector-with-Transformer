import collections
import heapq

class C1(object):

    def networkDelayTime(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a2)]
        for v3, v4, v5 in a1:
            v1[v3 - 1].append((v4 - 1, v5))
        v6 = 0
        v7 = set()
        v8 = collections.defaultdict(lambda: float('inf'))
        v8[a3 - 1] = 0
        v9 = [(0, a3 - 1)]
        while v9 and len(v7) != a2:
            v6, v3 = heapq.heappop(v9)
            v7.add(v3)
            if v8[v3] < v6:
                continue
            for v4, v5 in v1[v3]:
                if v4 in v7:
                    continue
                if v6 + v5 < v8[v4]:
                    v8[v4] = v6 + v5
                    heapq.heappush(v9, (v6 + v5, v4))
        return v6 if len(v7) == a2 else -1
