import heapq

class C1(object):

    def minTimeToReach(self, a1):
        """
        """

        def dijkstra(a1, a2):
            v1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            v2 = [[float('inf')] * len(a1[0]) for v3 in range(len(a1))]
            v2[a1[0]][a1[1]] = 0
            v4 = [(v2[a1[0]][a1[1]], a1[0], a1[1])]
            while v4:
                v5, v6, v7 = heapq.heappop(v4)
                if v5 != v2[v6][v7]:
                    continue
                if (v6, v7) == a2:
                    break
                for v8, v9 in v1:
                    v10, v11 = (v6 + v8, v7 + v9)
                    v12 = (v6 + v7) % 2 + 1
                    if not (0 <= v10 < len(a1) and 0 <= v11 < len(a1[0]) and (v2[v10][v11] > max(a1[v10][v11], v5) + v12)):
                        continue
                    v2[v10][v11] = max(a1[v10][v11], v5) + v12
                    heapq.heappush(v4, (v2[v10][v11], v10, v11))
            return v2[a2[0]][a2[1]]
        return dijkstra((0, 0), (len(a1) - 1, len(a1[0]) - 1))
