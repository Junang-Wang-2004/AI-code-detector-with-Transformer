class Solution:
    def minMoves2(self, nums):
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        mid = n // 2
        median = sorted_nums[mid]
        result = 0
        for i in range(mid):
            result += median - sorted_nums[i]
        for i in range(mid + 1, n):
            result += sorted_nums[i] - median
        return result
