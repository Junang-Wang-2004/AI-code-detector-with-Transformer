import heapq

class C1:

    def smallestChair(self, a1, a2):
        v1 = []
        for v2 in range(len(a1)):
            v3, v4 = a1[v2]
            v1.append((v3, 1, v2))
            v1.append((v4, 0, v2))
        v1.sort()
        v5 = []
        v6 = {}
        v7 = 0
        for v8, v9, v10 in v1:
            if v9 == 0:
                v11 = v6.pop(v10)
                heapq.heappush(v5, v11)
            else:
                v12 = heapq.heappop(v5) if v5 else v7
                if v12 == v7:
                    v7 += 1
                v6[v10] = v12
                if v10 == a2:
                    return v12
