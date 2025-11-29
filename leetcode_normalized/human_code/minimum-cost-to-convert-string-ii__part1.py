import collections
import itertools

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')
        v2 = collections.defaultdict(dict)
        for v3 in itertools.chain(a3, a4):
            v4 = len(v3)
            v5 = v2[v4]
            if v3 not in v5:
                v5[v3] = len(v5)

        def dijkstra(a1, a2):
            v1 = [v1] * len(a1)
            v1[a2] = 0
            v2 = [(0, a2)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                for v5, v6 in enumerate(a1[v4]):
                    if v1[v5] <= v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1
        v6 = {}

        def memoization(a1, a2, a3, a4):
            if a1 not in v6:
                v6[a1] = {}
            if a3 not in v6[a1]:
                v6[a1][a3] = dijkstra(a2, a3)
            return v6[a1][a3][a4]
        v7 = {v4: [[0 if u == v else v1 for v8 in range(len(v5))] for v9 in range(len(v5))] for v4, v5 in v2.items()}
        for v10 in range(len(a3)):
            v4 = len(a3[v10])
            v5, v11 = (v2[v4], v7[v4])
            v9, v8 = (v5[a3[v10]], v5[a4[v10]])
            v11[v9][v8] = min(v11[v9][v8], a5[v10])
        v12 = {len(v3) for v3 in a3}
        v13 = [v1] * (max((len(v3) for v3 in a3)) + 1)
        v13[0] = 0
        for v10 in range(len(a1)):
            if v13[v10 % len(v13)] == v1:
                continue
            if a1[v10] == a2[v10]:
                v13[(v10 + 1) % len(v13)] = min(v13[(v10 + 1) % len(v13)], v13[v10 % len(v13)])
            for v4 in v12:
                if v10 + v4 > len(a1):
                    continue
                v5, v11 = (v2[v4], v7[v4])
                v9, v8 = (a1[v10:v10 + v4], a2[v10:v10 + v4])
                if v9 in v5 and v8 in v5:
                    v13[(v10 + v4) % len(v13)] = min(v13[(v10 + v4) % len(v13)], v13[v10 % len(v13)] + memoization(v4, v11, v5[v9], v5[v8]))
            v13[v10 % len(v13)] = v1
        return v13[len(a1) % len(v13)] if v13[len(a1) % len(v13)] != v1 else -1
