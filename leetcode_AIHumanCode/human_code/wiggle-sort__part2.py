# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def wiggleSort(self, nums):
        """
        """
        nums.sort()
        med = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]
