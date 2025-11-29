# Time:  O(logr)
# Space: O(1)

# hash table, bit manipulations
class Solution(object):
    def minImpossibleOR(self, nums):
        """
        """
        lookup = set(nums)
        return next(1<<i for i in range(31) if 1<<i not in lookup)
