import collections
import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')
        v2 = {}
        for v3 in itertools.chain(a3, a4):
            if v3 in v2:
                continue
            v2[v3] = len(v2)

        def dijkstra(a1):
            v1 = {a1: 0}
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                if v4 not in dist:
                    continue
                for v5, v6 in dist[v4].items():
                    if v5 in v1 and v1[v5] <= v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1
        v4 = {}

        def memoization(a1, a2):
            if a1 not in v2:
                v4[a1] = dijkstra(a1)
            return v4[a1][a2] if a2 in v4[a1] else v1
        v5 = {}
        for v6 in range(len(a3)):
            v7, v8 = (v2[a3[v6]], v2[a4[v6]])
            if v7 not in v5:
                v5[v7] = {v8: v1}
            if v8 not in v5[v7]:
                v5[v7][v8] = v1
            v5[v7][v8] = min(v5[v7][v8], a5[v6])
        v9 = {len(v3) for v3 in a3}
        v10 = [v1] * (max((len(v3) for v3 in a3)) + 1)
        v10[0] = 0
        for v6 in range(len(a1)):
            if v10[v6 % len(v10)] == v1:
                continue
            if a1[v6] == a2[v6]:
                v10[(v6 + 1) % len(v10)] = min(v10[(v6 + 1) % len(v10)], v10[v6 % len(v10)])
            for v11 in v9:
                if v6 + v11 > len(a1):
                    continue
                v7, v8 = (a1[v6:v6 + v11], a2[v6:v6 + v11])
                if v7 in v2 and v8 in v2:
                    v10[(v6 + v11) % len(v10)] = min(v10[(v6 + v11) % len(v10)], v10[v6 % len(v10)] + memoization(v2[v7], v2[v8]))
            v10[v6 % len(v10)] = v1
        return v10[len(a1) % len(v10)] if v10[len(a1) % len(v10)] != v1 else -1
