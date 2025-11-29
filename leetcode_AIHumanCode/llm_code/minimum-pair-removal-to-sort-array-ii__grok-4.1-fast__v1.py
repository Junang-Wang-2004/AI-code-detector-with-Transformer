import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        values = [0] * (n + 2)
        prevv = [0] * (n + 2)
        nextt = [0] * (n + 2)
        for i in range(n + 2):
            prevv[i] = i - 1
            nextt[i] = i + 1
        for i in range(1, n + 1):
            values[i] = nums[i -
