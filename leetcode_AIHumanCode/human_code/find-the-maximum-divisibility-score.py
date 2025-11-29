# Time:  O(n * d)
# Space: O(1)

# brute force
class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        """
        return max(divisors, key=lambda d: (sum(x%d == 0 for x in nums), -d))
