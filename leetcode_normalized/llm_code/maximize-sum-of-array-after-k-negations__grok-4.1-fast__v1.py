import heapq

class C1:

    def largestSumAfterKNegations(self, a1, a2):
        heapq.heapify(a1)
        for v1 in range(a2):
            v2 = heapq.heappop(a1)
            heapq.heappush(a1, -v2)
        return sum(a1)
