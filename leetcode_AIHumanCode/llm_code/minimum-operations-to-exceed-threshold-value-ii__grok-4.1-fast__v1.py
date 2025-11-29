import heapq

class Solution(object):
    def minOperations(self, nums, k):
        minheap = []
        for val in nums:
            heapq.heappush(minheap, val)
        steps = 0
        while minheap and minheap[0] < k:
            x = heapq.heappop(minheap)
            y = heapq.heappop(minheap)
            heapq.heappush(minheap, 2 * x + y)
            steps += 1
        return steps
