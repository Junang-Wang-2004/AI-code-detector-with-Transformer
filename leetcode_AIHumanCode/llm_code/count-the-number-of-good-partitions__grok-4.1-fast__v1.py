class Solution:
    def numberOfGoodPartitions(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        last_idx = {}
        for i, val in enumerate(nums):
            last_idx[val] = i
        components = 0
        start = 0
        while start < n:
            components += 1
            end = last_idx[nums[start]]
            cursor = start
            while cursor <= end:
                end = max(end, last_idx[nums[cursor]])
                cursor += 1
            start = end + 1
        exp = max(0, components - 1)
        return pow(2, exp, MOD)
