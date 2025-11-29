class Solution(object):
    def maxValue(self, events, k):
        events.sort(key=lambda x: x[1])
        n = len(events)
        end_times = [ev[1] for ev in events]
        allowable_prefix = [0] * n
        for i in range(n):
            left, right = 0, i
            while left <= right:
                mid = left + (right - left) // 2
                if end_times[mid] < events[i][0]:
                    left = mid + 1
                else:
                    right = mid - 1
            allowable_prefix[i] = right + 1
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            p = allowable_prefix[i - 1]
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
            for j in range(1, k + 1):
                dp[i][j] = max(dp[i][j], dp[p][j - 1] + events[i - 1][2])
        return dp[n][k]
