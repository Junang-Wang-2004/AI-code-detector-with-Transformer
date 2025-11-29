import heapq

class C1(object):

    def minimumTime(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dijkstra(a1, a2):
            v1 = [[float('inf')] * len(a1[0]) for v2 in range(len(a1))]
            v1[a1[0]][a1[1]] = 0
            v3 = [(0, a1[0], a1[1])]
            while v3:
                v4, v5, v6 = heapq.heappop(v3)
                if v1[v5][v6] < v4:
                    continue
                if (v5, v6) == a2:
                    break
                for v7, v8 in v1:
                    v9, v10 = (v5 + v7, v6 + v8)
                    if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[0]) and (v1[v9][v10] > max(a1[v9][v10] + int(a1[v9][v10] % 2 == v1[v5][v6] % 2), v4 + 1))):
                        continue
                    v1[v9][v10] = max(a1[v9][v10] + int(a1[v9][v10] % 2 == v1[v5][v6] % 2), v4 + 1)
                    heapq.heappush(v3, (v1[v9][v10], v9, v10))
            return v1[a2[0]][a2[1]]
        if min(a1[0][1], a1[1][0]) > 1:
            return -1
        return dijkstra((0, 0), (len(a1) - 1, len(a1[0]) - 1))
