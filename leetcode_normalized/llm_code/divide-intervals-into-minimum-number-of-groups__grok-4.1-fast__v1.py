import heapq

class C1:

    def minGroups(self, a1):
        v1 = sorted(a1, key=lambda x: x[0])
        v2 = []
        v3 = 0
        for v4, v5 in v1:
            while v2 and v2[0] < v4:
                heapq.heappop(v2)
            heapq.heappush(v2, v5)
            v3 = max(v3, len(v2))
        return v3
