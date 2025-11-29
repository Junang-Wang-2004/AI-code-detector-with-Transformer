import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        n = len(quality)
        order = list(range(n))
        order.sort(key=lambda x: wage[x] / quality[x])
        heap = []
        total = 0
        minimum = float('inf')
        for idx in order:
            qval = quality[idx]
            rate = wage[idx] / qval
            total += qval
            heapq.heappush(heap, -qval)
            while len(heap) > K:
                total -= -heapq.heappop(heap)
            if len(heap) == K:
                minimum = min(minimum, total * rate)
        return minimum
