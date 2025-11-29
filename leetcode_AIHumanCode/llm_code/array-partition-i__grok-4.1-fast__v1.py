class Solution:
    def arrayPairSum(self, nums):
        sorted_nums = sorted(nums)
        total = 0
        idx = 0
        while idx < len(sorted_nums):
            total += sorted_nums[idx]
            idx += 2
        return total
