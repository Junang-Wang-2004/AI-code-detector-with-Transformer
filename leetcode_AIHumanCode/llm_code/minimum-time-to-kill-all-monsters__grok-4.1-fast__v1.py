class Solution:
    def minimumTime(self, power):
        m = len(power)
        N = 1 << m
        INF = float('inf')
        dp = [INF] * N
        dp[0] = 0
        for state in range(N):
            cnt = bin(state).count('1')
            for j in range(m):
                if state & (1 << j):
                    prev_state = state ^ (1 << j)
                    extra = (power[j] + cnt - 1) // cnt
                    dp[state] = min(dp[state], dp[prev_state] + extra)
        return int(dp[N - 1])
