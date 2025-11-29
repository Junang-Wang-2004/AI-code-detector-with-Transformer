# Time:  O((m * n) * (m + n) / 32)
# Space: O(n * (m + n) / 32)

# dp with bitsets
class Solution(object):
    def hasValidPath(self, grid):
        """
        """
        if (len(grid)+len(grid[0])-1)%2:
            return False
        dp = [0]*(len(grid[0])+1)
        for i in range(len(grid)):
            dp[0] = int(not i)
            for j in range(len(grid[0])):
                dp[j+1] = (dp[j]|dp[j+1])<<1 if grid[i][j] == '(' else (dp[j]|dp[j+1])>>1
        return dp[-1]&1


