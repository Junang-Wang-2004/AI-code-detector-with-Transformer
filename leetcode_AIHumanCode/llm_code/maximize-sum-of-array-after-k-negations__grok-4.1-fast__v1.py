import heapq

class Solution:
    def largestSumAfterKNegations(self, nums, k):
        heapq.heapify(nums)
        for _ in range(k):
            val = heapq.heappop(nums)
            heapq.heappush(nums, -val)
        return sum(nums)
