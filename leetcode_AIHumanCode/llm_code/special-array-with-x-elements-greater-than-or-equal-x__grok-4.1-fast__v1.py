class Solution:
    def specialArray(self, nums):
        size = len(nums)
        for val in range(size + 1):
            matches = sum(1 for x in nums if x >= val)
            if matches == val:
                return val
        return -1
