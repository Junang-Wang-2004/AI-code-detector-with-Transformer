class Solution:
    def findDuplicates(self, nums):
        found = []
        size = len(nums)
        for p in range(size):
            val = abs(nums[p])
            loc = val - 1
            if nums[loc] < 0:
                found.append(val)
            else:
                nums[loc] = -nums[loc]
        return found
