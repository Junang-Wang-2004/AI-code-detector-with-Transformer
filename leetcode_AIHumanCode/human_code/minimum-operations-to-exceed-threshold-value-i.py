# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def minOperations(self, nums, k):
        """
        """
        return sum(x < k for x in nums)
