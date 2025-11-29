from collections import deque

class Solution(object):
    def checkArray(self, nums, k):
        dq = deque()
        cover = 0
        for i in range(len(nums)):
            if nums[i] < cover:
                return False
            adj = nums[i] - cover
            cover += adj
            dq.append(adj)
            if i >= k - 1:
                cover -= dq.popleft()
        return cover == 0
