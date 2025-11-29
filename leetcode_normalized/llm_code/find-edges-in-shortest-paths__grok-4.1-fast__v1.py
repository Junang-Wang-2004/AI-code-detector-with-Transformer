import heapq

class C1:

    def findAnswer(self, a1, a2):
        v1 = float('inf')

        def shortest_distances(a1):
            v1 = [v1] * a1
            v1[a1] = 0
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                for v5, v6 in graph[v4]:
                    v7 = v3 + v6
                    if v7 < v1[v5]:
                        v1[v5] = v7
                        heapq.heappush(v2, (v7, v5))
            return v1
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = shortest_distances(0)
        v8 = shortest_distances(a1 - 1)
        v9 = v7[a1 - 1]
        v10 = []
        for v11, v12, v13 in a2:
            if v7[v11] < v1 and v8[v12] < v1 and (v7[v11] + v13 + v8[v12] == v9):
                v10.append(True)
                continue
            if v7[v12] < v1 and v8[v11] < v1 and (v7[v12] + v13 + v8[v11] == v9):
                v10.append(True)
            else:
                v10.append(False)
        return v10
