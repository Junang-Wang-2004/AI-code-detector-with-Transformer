class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        total = 0
        last = nums[0]
        for val in nums[1:]:
            target = last + 1
            if val < target:
                total += target - val
                last = target
            else:
                last = val
        return total
