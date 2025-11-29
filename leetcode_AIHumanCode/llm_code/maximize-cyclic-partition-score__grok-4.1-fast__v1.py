class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        min_idx = 0
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
        def compute(start):
            prices = nums[start:] + nums[:start]
            dp = [0] * (n + 1)
            res = 0
            for _ in range(k):
                ndp = [float('-inf')] * (n + 1)
                ndp[0] = 0
                hmax = float('-inf')
                cmax = float('-inf')
                for j in range(n):
                    p = prices[j]
                    hmax = max(hmax, dp[j] - p)
                    cmax = max(cmax, dp[j] + p)
                    ndp[j + 1] = max(ndp[j], hmax + p, cmax - p)
                dp = ndp
                res = max(res, dp[n])
            return res
        return max(compute(min_idx), compute((min_idx + 1) % n))
