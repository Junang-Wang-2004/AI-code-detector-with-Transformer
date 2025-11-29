# Time:  O(n * m * l)
# Space: O(n * m)
# dp
class Solution2(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        """
        MOD = 10**9+7
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        dp[0][0][0] = dp[0][0][1] = 1
        for i in range(zero+1):
            for j in range(one+1):
                for k in range(1, limit+1):
                    if i-k >= 0:
                        dp[i][j][0] = (dp[i][j][0]+dp[i-k][j][1])%MOD
                    if j-k >= 0:
                        dp[i][j][1] = (dp[i][j][1]+dp[i][j-k][0])%MOD
        return (dp[-1][-1][0]+dp[-1][-1][1])%MOD
