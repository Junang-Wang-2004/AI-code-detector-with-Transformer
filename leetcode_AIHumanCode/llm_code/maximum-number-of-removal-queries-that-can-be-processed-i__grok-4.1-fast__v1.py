class Solution(object):
    def maximumProcessableQueries(self, nums, queries):
        n = len(nums)
        m = len(queries)
        dp = [[-1] * n for _ in range(n)]
        dp[0][n - 1] = 0
        for segsize in range(n - 1, 0, -1):
            for left in range(n - segsize + 1):
                right = left + segsize - 1
                opts = []
                if left > 0 and dp[left - 1][right] >= 0:
                    prev = dp[left - 1][right]
                    extra = 1 if nums[left - 1] >= queries[prev] else 0
                    opts.append(prev + extra)
                if right < n - 1 and dp[left][right + 1] >= 0:
                    prev = dp[left][right + 1]
                    extra = 1 if nums[right + 1] >= queries[prev] else 0
                    opts.append(prev + extra)
                if opts:
                    dp[left][right] = max(opts)
                if dp[left][right] == m:
                    return m
        result = 0
        for idx in range(n):
            if dp[idx][idx] >= 0:
                prev = dp[idx][idx]
                extra = 1 if prev < m and nums[idx] >= queries[prev] else 0
                result = max(result, prev + extra)
        return result
