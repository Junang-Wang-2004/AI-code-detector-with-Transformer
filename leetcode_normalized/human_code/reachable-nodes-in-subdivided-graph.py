import collections
import heapq

class C1(object):

    def reachableNodes(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a3)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [(0, 0)]
        v7 = collections.defaultdict(lambda: float('inf'))
        v7[0] = 0
        v8 = collections.defaultdict(lambda: collections.defaultdict(int))
        v9 = 0
        while v6:
            v10, v3 = heapq.heappop(v6)
            if v7[v3] < v10:
                continue
            v9 += 1
            for v4, v5 in v1[v3]:
                v8[v3][v4] = min(v5, a2 - v10)
                v11 = v10 + v5 + 1
                if v11 <= a2 and v11 < v7[v4]:
                    v7[v4] = v11
                    heapq.heappush(v6, (v11, v4))
        for v3, v4, v5 in a1:
            v9 += min(v5, v8[v3][v4] + v8[v4][v3])
        return v9
