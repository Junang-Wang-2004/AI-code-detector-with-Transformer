class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        ptr = 0
        idx = 0
        while idx < n:
            if idx + 1 < n and nums[idx] == nums[idx + 1]:
                nums[ptr] = nums[idx] * 2
                ptr += 1
                idx += 2
            else:
                nums[ptr] = nums[idx]
                ptr += 1
                idx += 1
        while ptr < n:
            nums[ptr] = 0
            ptr += 1
        return nums
