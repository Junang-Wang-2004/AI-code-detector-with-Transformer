import heapq

class C1:

    def mostBooked(self, a1, a2):
        a2.sort()
        v1 = [(0, i) for v2 in range(a1)]
        heapq.heapify(v1)
        v3 = [0] * a1
        for v4, v5 in a2:
            while v1 and v1[0][0] < v4:
                v6, v7 = heapq.heappop(v1)
                heapq.heappush(v1, (v4, v7))
            v8, v7 = heapq.heappop(v1)
            v9 = v5 - v4
            heapq.heappush(v1, (v8 + v9, v7))
            v3[v7] += 1
        v10 = 0
        v11 = 0
        for v2 in range(a1):
            if v3[v2] > v10:
                v10 = v3[v2]
                v11 = v2
        return v11
