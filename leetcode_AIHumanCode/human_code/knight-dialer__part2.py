# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def knightDialer(self, N):
        """
        """
        M = 10**9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [[1 for _ in range(10)] for _ in range(2)]
        for i in range(N-1):
            dp[(i+1) % 2] = [0] * 10
            for j in range(10):
                for nei in moves[j]:
                    dp[(i+1) % 2][nei] += dp[i % 2][j]
                    dp[(i+1) % 2][nei] %= M
        return sum(dp[(N-1) % 2]) % M
