class Solution:
    def minimumCost(self, nums):
        first, second = float('inf'), float('inf')
        for val in nums[1:]:
            if val < first:
                second = first
                first = val
            elif val < second:
                second = val
        return nums[0] + first + second
