# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def minMoves(self, nums):
        """
        """
        return max(nums)*len(nums)-sum(nums)
