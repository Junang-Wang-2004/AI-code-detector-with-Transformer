import heapq

class C1(object):

    def minOperations(self, a1, a2):
        v1 = []
        for v2 in a1:
            heapq.heappush(v1, v2)
        v3 = 0
        while v1 and v1[0] < a2:
            v4 = heapq.heappop(v1)
            v5 = heapq.heappop(v1)
            heapq.heappush(v1, 2 * v4 + v5)
            v3 += 1
        return v3
