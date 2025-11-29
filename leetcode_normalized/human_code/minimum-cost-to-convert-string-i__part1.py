import heapq

class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')

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
        v2 = {}

        def memoization(a1, a2):
            if a1 not in v2:
                v2[a1] = dijkstra(a1)
            return v2[a1][a2] if a2 in v2[a1] else v1
        v3 = {}
        for v4 in range(len(a3)):
            v5, v6 = (ord(a3[v4]) - ord('a'), ord(a4[v4]) - ord('a'))
            if v5 not in v3:
                v3[v5] = {v6: v1}
            if v6 not in v3[v5]:
                v3[v5][v6] = v1
            v3[v5][v6] = min(v3[v5][v6], a5[v4])
        v7 = sum((memoization(ord(a1[v4]) - ord('a'), ord(a2[v4]) - ord('a')) for v4 in range(len(a1))))
        return v7 if v7 != v1 else -1
