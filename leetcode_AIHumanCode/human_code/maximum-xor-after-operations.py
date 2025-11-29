from functools import reduce
# Time:  O(n)
# Space: O(1)

# bit manipulation
class Solution(object):
    def maximumXOR(self, nums):
        """
        """
        return reduce(lambda x, y: x|y, nums)
