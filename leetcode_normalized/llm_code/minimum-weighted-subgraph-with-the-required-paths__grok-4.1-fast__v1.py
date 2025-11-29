import heapq

class C1:

    def minimumWeight(self, a1, a2, a3, a4, a5):
        v1 = [[] for v2 in range(a1)]
        v3 = [[] for v2 in range(a1)]
        for v4, v5, v6 in a2:
            v1[v4].append((v5, v6))
            v3[v5].append((v4, v6))

        def shortest_paths(a1, a2):
            v1 = [float('inf')] * a1
            v1[a2] = 0
            v2 = [(0, a2)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                for v5, v6 in a1[v4]:
                    v7 = v3 + v6
                    if v7 < v1[v5]:
                        v1[v5] = v7
                        heapq.heappush(v2, (v7, v5))
            return v1
        v7 = shortest_paths(v1, a3)
        v8 = shortest_paths(v1, a4)
        v9 = shortest_paths(v3, a5)
        v10 = float('inf')
        for v11 in range(a1):
            v12 = v7[v11] + v8[v11] + v9[v11]
            if v12 < v10:
                v10 = v12
        return v10 if v10 < float('inf') else -1
