# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        """
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            hold1 = max(hold1, -i)
            release1 = max(release1, hold1 + i)
            hold2 = max(hold2, release1 - i)
            release2 = max(release2, hold2 + i)
        return release2


