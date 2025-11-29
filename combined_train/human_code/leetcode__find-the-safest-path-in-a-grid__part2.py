import heapq

class C1(object):

    def maximumSafenessFactor(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs():
            v1 = [[0 if a1[r][c] == 1 else -1 for v2 in range(len(a1[0]))] for v3 in range(len(a1))]
            v4 = [(v3, v2) for v3 in range(len(a1)) for v2 in range(len(a1[0])) if a1[v3][v2]]
            v5 = 0
            while v4:
                v6 = []
                for v3, v2 in v4:
                    for v7, v8 in v1:
                        v9, v10 = (v3 + v7, v2 + v8)
                        if not (0 <= v9 < len(v1) and 0 <= v10 < len(v1[0]) and (v1[v9][v10] == -1)):
                            continue
                        v1[v9][v10] = v5 + 1
                        v6.append((v9, v10))
                v4 = v6
                v5 += 1
            return v1

        def dijkstra(a1, a2):
            v1 = [(-dist[a1[0]][a1[1]], a1)]
            dist[a1[0]][a1[1]] = -1
            while v1:
                v2, v3 = heapq.heappop(v1)
                v2 = -v2
                if v3 == a2:
                    return v2
                for v4, v5 in v1:
                    v6, v7 = (v3[0] + v4, v3[1] + v5)
                    if not (0 <= v6 < len(dist) and 0 <= v7 < len(dist[0]) and (dist[v6][v7] != -1)):
                        continue
                    heapq.heappush(v1, (-min(v2, dist[v6][v7]), (v6, v7)))
                    dist[v6][v7] = -1
            return -1
        v2 = bfs()
        return dijkstra(v2, (0, 0), (len(a1) - 1, len(a1[0]) - 1))
