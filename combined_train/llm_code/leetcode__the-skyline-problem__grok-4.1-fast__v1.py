import heapq

class C1:

    def getSkyline(self, a1):
        if not a1:
            return []
        v1 = []
        for v2, v3, v4 in a1:
            v1.append((v2, -v4, v3))
            v1.append((v3, 0, 0))
        v1.sort(key=lambda p: (p[0], p[1]))
        v5 = []
        v6 = []
        v7 = 0
        v8 = 0
        v9 = len(v1)
        while v8 < v9:
            v10 = v1[v8][0]
            while v8 < v9 and v1[v8][0] == v10 and (v1[v8][1] < 0):
                v11, v12, v13 = v1[v8]
                heapq.heappush(v5, (v12, v13))
                v8 += 1
            while v8 < v9 and v1[v8][0] == v10:
                v8 += 1
            while v5 and v5[0][1] <= v10:
                heapq.heappop(v5)
            v14 = -v5[0][0] if v5 else 0
            if v14 != v7:
                v6.append([v10, v14])
                v7 = v14
        return v6
