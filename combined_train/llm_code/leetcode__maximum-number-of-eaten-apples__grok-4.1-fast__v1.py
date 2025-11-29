import heapq

class C1:

    def eatenApples(self, a1, a2):
        v1 = []
        v2 = 0
        v3 = 0
        v4 = len(a1)
        v5 = a1[:]
        while v3 < v4 or v1:
            if v3 < v4 and v5[v3] > 0:
                heapq.heappush(v1, (v3 + a2[v3], v3))
            while v1 and v1[0][0] <= v3:
                heapq.heappop(v1)
            if v1:
                v6, v7 = v1[0]
                v5[v7] -= 1
                if v5[v7] == 0:
                    heapq.heappop(v1)
                v2 += 1
            v3 += 1
        return v2
