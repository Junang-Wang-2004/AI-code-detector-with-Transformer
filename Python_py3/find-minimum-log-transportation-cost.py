# Time:  O(1)
# Space: O(1)

# math
class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        """
        return k*max(n-k, m-k, 0)
