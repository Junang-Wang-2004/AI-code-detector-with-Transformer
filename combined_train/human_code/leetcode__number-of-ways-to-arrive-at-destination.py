import heapq

class C1(object):

    def countPaths(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def dijkstra(a1, a2, a3):
            v1 = collections.defaultdict(lambda: float('inf'))
            v1[a2] = 0
            v2 = [(0, a2)]
            v3 = [0] * len(a1)
            v3[0] = 1
            while v2:
                v4, v5 = heapq.heappop(v2)
                if v1[v5] < v4:
                    continue
                if v5 == a3:
                    break
                for v6, v7 in a1[v5]:
                    if v6 in v1 and v1[v6] <= v4 + v7:
                        if v1[v6] == v4 + v7:
                            v3[v6] = (v3[v6] + v3[v5]) % v1
                        continue
                    v3[v6] = v3[v5]
                    v1[v6] = v4 + v7
                    heapq.heappush(v2, (v4 + v7, v6))
            return v3[a3]
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        return dijkstra(v2, 0, a1 - 1)
