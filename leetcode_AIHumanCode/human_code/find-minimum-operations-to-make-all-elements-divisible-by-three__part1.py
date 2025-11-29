# Time:  O(n)
# Space: O(1)

# math
class Solution(object):
    def minimumOperations(self, nums):
        """
        """
        return sum(x%3 != 0 for x in nums)


