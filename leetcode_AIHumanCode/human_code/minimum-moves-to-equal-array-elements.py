# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minMoves(self, nums):
        """
        """
        return sum(nums) - len(nums) * min(nums)

