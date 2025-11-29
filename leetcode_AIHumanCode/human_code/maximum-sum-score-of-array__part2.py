# Time:  O(n)
# Space: O(1)
# prefix sum
class Solution2(object):
    def maximumSumScore(self, nums):
        """
        """
        total = sum(nums)
        prefix = 0
        result = float("-inf")
        for x in nums:
            prefix += x
            result = max(result, prefix, total-prefix+x)
        return result
