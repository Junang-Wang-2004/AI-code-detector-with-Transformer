# Time:  O(n * w1 * w2)
# Space: O(w1 * w2)
# dp
class Solution2(object):
    def maxWeight(self, weights, w1, w2):
        """
        """
        dp = [[False]*(w2+1) for _ in range(w1+1)]
        dp[0][0] = True
        for w in weights:
            dp = [[dp[i][j] or (i-w >= 0 and dp[i-w][j]) or (j-w >= 0 and dp[i][j-w]) for j in range(w2+1)] for i in range(w1+1)]
        return max(i+j for i in range(w1+1) for j in range(w2+1) if dp[i][j])
