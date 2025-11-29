class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        full = (1 << n) - 1
        subsum = [0] * (1 << n)
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    subsum[mask] += jobs[i]
        def feasible(cap):
            dp = [k + 1] * (1 << n)
            dp[0] = 0
            for mask in range(1, 1 << n):
                s = mask
                while s > 0:
                    if subsum[s] <= cap:
                        prev = mask ^ s
                        dp[mask] = min(dp[mask], dp[prev] + 1)
                    s = (s - 1) & mask
            return dp[full] <= k
        left, right = max(jobs), sum(jobs)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
