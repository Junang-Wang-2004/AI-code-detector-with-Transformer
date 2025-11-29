# Time:  O(n)
# Space: O(1)

# dp
class Solution(object):
    def climbStairs(self, n, costs):
        """
        """
        a, b, c = float("inf"), float("inf"), 0
        for i in range(n):
            a, b, c = b, c, costs[i]+min(a+3**2, b+2**2, c+1**2)
        return c


