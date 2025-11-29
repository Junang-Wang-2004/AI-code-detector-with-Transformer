class Solution:
    def maxSizeSlices(self, slices):
        n = len(slices)
        k = n // 3
        
        def max_non_adjacent(start, end):
            length = end - start
            if length <= 0:
                return 0
            dp = [[0] * (k + 1) for _ in range(length + 1)]
            for i in range(1, length + 1):
                value = slices[start + i - 1]
                for cnt in range(k + 1):
                    dp[i][cnt] = dp[i - 1][cnt]
                    if cnt > 0:
                        prev_take = dp[i - 2][cnt - 1] if i >= 2 else 0
                        dp[i][cnt] = max(dp[i][cnt], value + prev_take)
            return dp[length][k]
        
        return max(max_non_adjacent(0, n - 1), max_non_adjacent(1, n))
