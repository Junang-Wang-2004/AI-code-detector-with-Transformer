import heapq

class Solution:
    def minOperations(self, nums, target):
        cursum = sum(num for num in nums)
        if cursum < target:
            return -1
        pq = []
        for num in nums:
            if num:
                heapq.heappush(pq, -num)
        ops = 0
        need = target
        while need > 0 and pq:
            top = -heapq.heappop(pq)
            if top <= need:
                need -= top
                cursum -= top
            elif cursum - top >= need:
                cursum -= top
            else:
                h = top // 2
                if h:
                    heapq.heappush(pq, -h)
                    heapq.heappush(pq, -h)
                ops += 1
        return ops
