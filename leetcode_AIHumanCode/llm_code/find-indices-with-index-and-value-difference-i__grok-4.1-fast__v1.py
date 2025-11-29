class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        n = len(nums)
        max_idx = 0
        min_idx = 0
        for pos in range(n - indexDifference):
            if nums[pos] > nums[max_idx]:
                max_idx = pos
            if nums[pos] < nums[min_idx]:
                min_idx = pos
            j = pos + indexDifference
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
        return [-1, -1]
