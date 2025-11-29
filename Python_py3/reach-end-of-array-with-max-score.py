# Time:  O(n)
# Space: O(1)

# greedy
class Solution(object):
    def findMaximumScore(self, nums):
        """
        """
        result = mx = 0
        for x in nums:
            result += mx
            mx = max(mx, x)
        return result
