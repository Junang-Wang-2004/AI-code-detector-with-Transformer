from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        q = deque()
        output = []
        for j in range(k):
            while q and nums[q[-1]] <= nums[j]:
                q.pop()
            q.append(j)
        output.append(nums[q[0]])
        for j in range(k, len(nums)):
            if q[0] == j - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[j]:
                q.pop()
            q.append(j)
            output.append(nums[q[0]])
        return output
