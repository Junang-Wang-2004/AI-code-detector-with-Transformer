class Solution:
    def minimumAddedCoins(self, nums, target):
        nums.sort()
        count = 0
        extent = 0
        idx = 0
        n = len(nums)
        while extent < target:
            if idx < n and nums[idx] <= extent + 1:
                extent += nums[idx]
                idx += 1
            else:
                count += 1
                extent = 2 * extent + 1
        return count
