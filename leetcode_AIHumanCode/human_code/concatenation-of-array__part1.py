# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getConcatenation(self, nums):
        """
        """
        nums.extend(nums)
        return nums


