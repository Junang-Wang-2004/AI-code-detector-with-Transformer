import heapq

class Solution:
    def rangeSum(self, nums, n, left, right):
        MOD = 10**9 + 7
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], i))
        res = 0
        for k in range(right):
            val, pos = heapq.heappop(pq)
            if k + 1 >= left:
                res = (res + val) % MOD
            if pos < n - 1:
                heapq.heappush(pq, (val + nums[pos + 1], pos + 1))
        return res
