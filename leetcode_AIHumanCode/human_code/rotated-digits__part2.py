# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def rotatedDigits(self, N):
        """
        """
        INVALID, SAME, DIFF = 0, 1, 2
        same, diff = [0, 1, 8], [2, 5, 6, 9]
        dp = [0] * (N+1)
        dp[0] = SAME
        for i in range(N//10+1):
            if dp[i] != INVALID:
                for j in same:
                    if i*10+j <= N:
                        dp[i*10+j] = max(SAME, dp[i])
                for j in diff:
                    if i*10+j <= N:
                        dp[i*10+j] = DIFF
        return dp.count(DIFF)


