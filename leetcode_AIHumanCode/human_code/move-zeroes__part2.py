# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def moveZeroes(self, nums):
        """
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0


