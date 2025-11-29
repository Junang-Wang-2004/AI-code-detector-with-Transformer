# Time:  O(n)
# Space: O(1)
# math
class Solution2(object):
    def minimumOperations(self, nums):
        """
        """
        return sum(min(x%3, 3-x%3) for x in nums)
