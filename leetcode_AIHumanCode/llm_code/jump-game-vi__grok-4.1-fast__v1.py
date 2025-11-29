from collections import deque

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        values = [0] * n
        values[0] = nums[0]
        candidates = deque([0])
        for pos in range(1, n):
            while candidates and candidates[0] < pos - k:
                candidates.popleft()
            values[pos] = nums[pos] + values[candidates[0]]
            while candidates and values[candidates[-1]] <= values[pos]:
                candidates.pop()
            candidates.append(pos)
        return values[-1]
