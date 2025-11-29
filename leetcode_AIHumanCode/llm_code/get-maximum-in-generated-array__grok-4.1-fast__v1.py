class Solution:
    def getMaximumGenerated(self, n):
        memo = {}
        ans = 0
        for idx in range(n + 1):
            if idx == 0:
                val = 0
            elif idx == 1:
                val = 1
            else:
                h = idx // 2
                val = memo[h] if idx % 2 == 0 else memo[h] + memo[h + 1]
            memo[idx] = val
            if val > ans:
                ans = val
        return ans
