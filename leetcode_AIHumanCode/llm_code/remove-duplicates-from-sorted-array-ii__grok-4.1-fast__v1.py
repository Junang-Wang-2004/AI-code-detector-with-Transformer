class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        pos = 2
        for idx in range(2, n):
            if nums[idx] != nums[pos - 2]:
                nums[pos] = nums[idx]
                pos += 1
        return pos
