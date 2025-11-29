import heapq

class C1:

    def assignTasks(self, a1, a2):
        v1 = [(w, i) for v2, v3 in enumerate(a1)]
        heapq.heapify(v1)
        v4 = []
        v5 = []
        v6 = 0
        for v7 in range(len(a2)):
            v6 = max(v6, v7)
            while v4 and v4[0][0] <= v6:
                v8, v9, v10 = heapq.heappop(v4)
                heapq.heappush(v1, (v9, v10))
            if not v1:
                v6 = v4[0][0]
                while v4 and v4[0][0] <= v6:
                    v8, v9, v10 = heapq.heappop(v4)
                    heapq.heappush(v1, (v9, v10))
            v9, v10 = heapq.heappop(v1)
            v11 = v6 + a2[v7]
            heapq.heappush(v4, (v11, v9, v10))
            v5.append(v10)
        return v5
