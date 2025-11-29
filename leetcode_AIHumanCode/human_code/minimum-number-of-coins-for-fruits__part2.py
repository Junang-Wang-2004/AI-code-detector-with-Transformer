# Time:  O(nlogn)
# Space: O(n)
# dp, sorted list
from sortedcontainers import SortedList


class Solution2(object):
    def minimumCoins(self, prices):
        """
        """
        dp = [float("inf")]*(len(prices)+1)
        dp[0] = 0
        sl = SortedList()
        j = 0
        for i in range(len(prices)):
            sl.add((dp[i]+prices[i], i))
            while j+(j+1) < i:
                sl.remove(((dp[j]+prices[j], j)))
                j += 1
            dp[i+1] = sl[0][0]
        return dp[-1]


