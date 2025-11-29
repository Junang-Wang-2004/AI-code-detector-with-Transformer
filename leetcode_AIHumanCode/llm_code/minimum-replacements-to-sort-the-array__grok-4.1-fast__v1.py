class Solution:
    def minimumReplacement(self, nums):
        total = 0
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            num = nums[i]
            splits = (num + prev - 1) // prev
            total += splits - 1
            prev = num // splits
        return total
