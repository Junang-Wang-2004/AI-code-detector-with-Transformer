import heapq

class C1:

    def modifiedGraphEdges(self, a1, a2, a3, a4, a5):
        v1 = [[] for v2 in range(a1)]
        v3 = [[] for v2 in range(a1)]
        for v4, v5, v6 in a2:
            if v6 != -1:
                v1[v4].append((v5, v6))
                v1[v5].append((v4, v6))
                v3[v4].append((v5, v6))
                v3[v5].append((v4, v6))
            else:
                v1[v4].append((v5, 1))
                v1[v5].append((v4, 1))

        def shortest(a1, a2):
            v1 = float('inf')
            v2 = [v1] * a1
            v2[a2] = 0
            v3 = [(0, a2)]
            while v3:
                v4, v5 = heapq.heappop(v3)
                if v4 > v2[v5]:
                    continue
                for v6, v7 in a1[v5]:
                    v8 = v2[v5] + v7
                    if v8 < v2[v6]:
                        v2[v6] = v8
                        heapq.heappush(v3, (v8, v6))
            return v2
        v7 = shortest(v1, a3)
        if v7[a4] > a5:
            return []
        v8 = shortest(v3, a4)
        if v8[a3] < a5:
            return []
        for v4, v5, v6 in a2:
            if v6 == -1:
                v9 = a5 - v7[v4] - v8[v5]
                v10 = a5 - v7[v5] - v8[v4]
                a2[a2.index([v4, v5, v6])][2] = max(v9, v10, 1)
        return a2
