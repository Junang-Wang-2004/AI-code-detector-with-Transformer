# Time:  O(n)
# Space: O(1)

# bit manipulation
class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        """
        return sum(x%2 == 0 for x in nums) >= 2
