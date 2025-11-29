class Solution:
    def minNumberOfSemesters(self, n, dependencies, k):
        prereqs = [0] * n
        for pre, post in dependencies:
            prereqs[post - 1] |= 1 << (pre - 1)
        INF = n + 1
        dp = [INF] * (1 << n)
        dp[0] = 0
        pop = [0] * (1 << n)
        for i in range(1 << n):
            pop[i] = pop[i // 2] + (i & 1)
        for state in range(1 << n):
            if dp[state] == INF:
                continue
            ready = 0
            for i in range(n):
                if (state & (1 << i)) == 0 and (state & prereqs[i]) == prereqs[i]:
                    ready |= 1 << i
            num_ready = pop[ready]
            target = min(num_ready, k)
            sub = ready
            while sub:
                if pop[sub] == target:
                    nxt = state | sub
                    dp[nxt] = min(dp[nxt], dp[state] + 1)
                sub = (sub - 1) & ready
        return dp[(1 << n) - 1]
