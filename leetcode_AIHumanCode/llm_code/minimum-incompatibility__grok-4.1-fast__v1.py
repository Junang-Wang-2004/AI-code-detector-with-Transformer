class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        if n % k != 0:
            return -1
        group_size = n // k
        N = 1 << n
        INF = 10**18 + 5
        pop = [bin(i).count('1') for i in range(N)]
        cand = [INF] * N
        for mask in range(N):
            if pop[mask] == group_size:
                selected = [nums[i] for i in range(n) if mask & (1 << i)]
                if len(set(selected)) == group_size:
                    cand[mask] = max(selected) - min(selected)
        dp = [INF] * N
        dp[0] = 0
        for mask in range(N):
            if pop[mask] % group_size != 0:
                continue
            submask = mask
            while submask:
                if cand[submask] < INF:
                    prev = mask ^ submask
                    dp[mask] = min(dp[mask], dp[prev] + cand[submask])
                submask = (submask - 1) & mask
        res = dp[N - 1]
        return res if res < INF else -1
