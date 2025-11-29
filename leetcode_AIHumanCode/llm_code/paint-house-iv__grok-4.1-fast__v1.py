class Solution:
    def minCost(self, n, cost):
        m = len(cost[0])
        dp_prev = [[0] * m for _ in range(m)]
        rounds = n // 2
        for t in range(rounds):
            dp_curr = [[float('inf')] * m for _ in range(m)]
            costs_first = cost[t]
            costs_second = cost[n - 1 - t]
            for pos1 in range(m):
                for pos2 in range(m):
                    if pos1 == pos2:
                        continue
                    best_prior = float('inf')
                    for prev1 in range(m):
                        if prev1 == pos1:
                            continue
                        for prev2 in range(m):
                            if prev2 == pos2 or prev1 == prev2:
                                continue
                            best_prior = min(best_prior, dp_prev[prev1][prev2])
                    dp_curr[pos1][pos2] = best_prior + costs_first[pos1] + costs_second[pos2]
            dp_prev = dp_curr
        result = float('inf')
        for i in range(m):
            for j in range(m):
                if i != j:
                    result = min(result, dp_prev[i][j])
        return result
