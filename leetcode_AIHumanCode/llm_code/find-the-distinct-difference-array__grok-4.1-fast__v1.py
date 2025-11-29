class Solution:
    def distinctDifferenceArray(self, nums):
        n = len(nums)
        prefix = [0] * n
        left_seen = set()
        for i in range(n):
            left_seen.add(nums[i])
            prefix[i] = len(left_seen)
        suffix = [0] * n
        right_seen = set()
        for i in range(n - 1, -1, -1):
            right_seen.add(nums[i])
            suffix[i] = len(right_seen)
        return [prefix[i] - (suffix[i + 1] if i + 1 < n else 0) for i in range(n)]
