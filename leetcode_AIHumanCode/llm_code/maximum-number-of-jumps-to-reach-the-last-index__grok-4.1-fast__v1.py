class Solution(object):
    def maximumJumps(self, nums, target):
        n = len(nums)
        farthest = [float('-inf')] * n
        farthest[0] = 0
        for curr in range(n):
            if farthest[curr] == float('-inf'):
                continue
            for nxt in range(curr + 1, n):
                if abs(nums[nxt] - nums[curr]) <= target:
                    farthest[nxt] = max(farthest[nxt], farthest[curr] + 1)
        res = farthest[-1]
        return res if res != float('-inf') else -1
