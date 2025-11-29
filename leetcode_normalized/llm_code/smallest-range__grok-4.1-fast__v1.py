import heapq

class C1:

    def smallestRange(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = float('-inf')
        for v3, v4 in enumerate(a1):
            heapq.heappush(v1, (v4[0], v3, 0))
            v2 = max(v2, v4[0])
        v5 = float('inf')
        v6 = (0, 0)
        v7 = v1[0][0]
        if v2 - v7 < v5:
            v5 = v2 - v7
            v6 = (v7, v2)
        while v1:
            v8, v9, v10 = heapq.heappop(v1)
            if v10 + 1 == len(a1[v9]):
                break
            v11 = a1[v9][v10 + 1]
            heapq.heappush(v1, (v11, v9, v10 + 1))
            v2 = max(v2, v11)
            v7 = v1[0][0]
            v12 = v2 - v7
            if v12 < v5:
                v5 = v12
                v6 = (v7, v2)
        return v6
