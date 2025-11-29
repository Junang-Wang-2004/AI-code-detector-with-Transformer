import heapq

class C1:

    def maxEvents(self, a1):
        a1.sort(key=lambda x: x[0])
        v1 = []
        v2 = 0
        v3 = 1
        v4 = 0
        v5 = max((x[1] for v6 in a1))
        v7 = len(a1)
        while v3 <= v5:
            while v4 < v7 and a1[v4][0] <= v3:
                heapq.heappush(v1, a1[v4][1])
                v4 += 1
            while v1 and v1[0] < v3:
                heapq.heappop(v1)
            if v1:
                heapq.heappop(v1)
                v2 += 1
            v3 += 1
        return v2
