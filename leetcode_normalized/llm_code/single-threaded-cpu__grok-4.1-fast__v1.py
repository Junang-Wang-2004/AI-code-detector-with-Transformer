import heapq

class C1:

    def getOrder(self, a1):
        v1 = len(a1)
        v2 = sorted(((a1[j][0], a1[j][1], j) for v3 in range(v1)))
        v4 = []
        v5 = []
        v6 = v2[0][0]
        v7 = 0
        while v7 < v1 or v4:
            while v7 < v1 and v2[v7][0] <= v6:
                v8, v9, v10 = v2[v7]
                heapq.heappush(v4, (v9, v10))
                v7 += 1
            if v4:
                v9, v10 = heapq.heappop(v4)
                v6 += v9
                v5.append(v10)
            else:
                v6 = v2[v7][0]
        return v5
