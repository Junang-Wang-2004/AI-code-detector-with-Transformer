from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        overall_max = float('-inf')
        window = deque()
        for idx in range(len(nums)):
            while window and window[0][0] < idx - k:
                window.popleft()
            prev_max = window[0][1] if window else 0
            here = nums[idx] + prev_max
            while window and window[-1][1] <= here:
                window.pop()
            if here > 0:
                window.append((idx, here))
            overall_max = max(overall_max, here)
        return overall_max
