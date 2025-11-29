import heapq

class Solution:
    def makePrefSumNonNegative(self, nums):
        pq = []
        total = 0
        ops = 0
        for val in nums:
            heapq.heappush(pq, val)
            total += val
            if total < 0:
                total -= heapq.heappop(pq)
                ops += 1
        return ops
