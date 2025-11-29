# Time:  O(n * k)
# Space: O(k)
# dp
class Solution2(object):
    def countOfArrays(self, n, m, k):
        """
        """
        MOD = 10**9+7
        even, odd = m//2, (m+1)//2
        dp = [[0]*(k+1) for _ in range(2)]
        dp[0][0], dp[1][0] = even, odd
        for _ in range(n-1):
            for i in reversed(range(k+1)):
                dp[0][i], dp[1][i] = (((dp[0][i-1] if i-1 >= 0 else 0)+dp[1][i])*even)%MOD, ((dp[0][i]+dp[1][i])*odd)%MOD
        return (dp[0][k]+dp[1][k])%MOD
