class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        INF = float('inf')
        prev_dp = [[INF] * n for _ in range(target)]
        cand0 = range(n) if houses[0] == 0 else [houses[0] - 1]
        for col in cand0:
            prev_dp[0][col] = cost[0][col] if houses[0] == 0 else 0
        for idx in range(1, m):
            curr_dp = [[INF] * n for _ in range(target)]
            for grp in range(target):
                for pcol in range(n):
                    if prev_dp[grp][pcol] == INF:
                        continue
                    cand = range(n) if houses[idx] == 0 else [houses[idx] - 1]
                    for ncol in cand:
                        newgrp = grp + (pcol != ncol)
                        if newgrp >= target:
                            continue
                        extra = cost[idx][ncol] if houses[idx] == 0 else 0
                        curr_dp[newgrp][ncol] = min(curr_dp[newgrp][ncol], prev_dp[grp][pcol] + extra)
            prev_dp = curr_dp
        ans = min(prev_dp[target - 1])
        return ans if ans < INF else -1
