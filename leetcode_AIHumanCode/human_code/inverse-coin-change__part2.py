# Time:  O(n^2)
# Space: O(n)
# dp
class Solution2(object):
    def findCoins(self, numWays):
        """
        """
        result = []
        dp = [0]*(len(numWays)+1)
        dp[0] = 1
        for i in range(1, len(numWays)+1):
            if numWays[i-1]-dp[i] == 1:
                result.append(i)
                for j in range(i, len(numWays)+1):
                    dp[j] += dp[j-i]
            if numWays[i-1]-dp[i]:
                return []
        return result
