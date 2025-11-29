class Solution:
    def maxRemovals(self, source, pattern, targetIndices):
        m = len(pattern)
        dp = [float('inf')] * (m + 1)
        dp[0] = 0
        can_remove = set(targetIndices)
        for i, ch in enumerate(source):
            cost = 1 if i in can_remove else 0
            for j in range(m, 0, -1):
                if pattern[j - 1] == ch:
                    dp[j] = min(dp[j], dp[j - 1] + cost)
        return len(targetIndices) - dp[m]
