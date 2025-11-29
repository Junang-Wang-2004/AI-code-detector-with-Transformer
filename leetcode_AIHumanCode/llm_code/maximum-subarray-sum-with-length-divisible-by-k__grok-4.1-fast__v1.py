from collections import deque

class Solution(object):
    def maxSubarraySum(self, nums, k):
        q = deque([(0, 0)])
        pref = 0
        res = float('-inf')
        for i in range(len(nums)):
            pref += nums[i]
            idx = i + 1
            while q and q[0][0] < idx - k:
                q.popleft()
            res = max(res, pref - q[0][1])
            while q and q[-1][1] >= pref:
                q.pop()
            q.append((idx, pref))
        return res
