class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        idx = 0
        while idx < n:
            tgt = nums[idx] - 1
            if 0 <= tgt < n and nums[tgt] != nums[idx]:
                nums[idx], nums[tgt] = nums[tgt], nums[idx]
            else:
                idx += 1
        idx = 0
        while idx < n and nums[idx] == idx + 1:
            idx += 1
        return idx + 1
