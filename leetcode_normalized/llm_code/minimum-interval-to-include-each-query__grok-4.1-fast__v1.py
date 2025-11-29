import heapq

class C1:

    def minInterval(self, a1, a2):
        a1.sort(key=lambda x: x[0])
        v1 = sorted(enumerate(a2), key=lambda p: p[1])
        v2 = []
        v3 = 0
        v4 = [-1] * len(a2)
        for v5, v6 in v1:
            while v3 < len(a1) and a1[v3][0] <= v6:
                v7, v8 = a1[v3]
                heapq.heappush(v2, (v8 - v7 + 1, v8))
                v3 += 1
            while v2 and v2[0][1] < v6:
                heapq.heappop(v2)
            if v2:
                v4[v5] = v2[0][0]
        return v4
