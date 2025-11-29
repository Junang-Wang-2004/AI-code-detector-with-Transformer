import heapq

class C1:

    def cutOffTree(self, a1):
        if not a1:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] > 1:
                    v3.append((a1[v4][v5], v4, v5))
        v3.sort()

        def shortest_distance(a1, a2, a3, a4):
            if a1 == a3 and a2 == a4:
                return 0
            v1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            v2 = []
            heapq.heappush(v2, (abs(a1 - a3) + abs(a2 - a4), 0, a1, a2))
            v3 = set()
            while v2:
                v4, v5, v6, v7 = heapq.heappop(v2)
                v8 = (v6, v7)
                if v8 in v3:
                    continue
                v3.add(v8)
                if v6 == a3 and v7 == a4:
                    return v5
                for v9, v10 in v1:
                    v11, v12 = (v6 + v9, v7 + v10)
                    if 0 <= v11 < v1 and 0 <= v12 < v2 and (a1[v11][v12] > 0):
                        v13 = (v11, v12)
                        if v13 not in v3:
                            v14 = abs(v11 - a3) + abs(v12 - a4)
                            v15 = v5 + 1 + v14
                            heapq.heappush(v2, (v15, v5 + 1, v11, v12))
            return -1
        v6, v7 = (0, 0)
        v8 = 0
        for v9, v10, v11 in v3:
            v12 = shortest_distance(v6, v7, v10, v11)
            if v12 == -1:
                return -1
            v8 += v12
            v6, v7 = (v10, v11)
        return v8
