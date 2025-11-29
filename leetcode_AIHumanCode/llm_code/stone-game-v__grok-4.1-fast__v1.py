class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        score = [[0] * n for _ in range(n)]
        remain = [[0] * n for _ in range(n)]
        for i in range(n):
            remain[i][i] = stoneValue[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_cost = float('inf')
                best_remain = 0
                for k in range(i, j):
                    left = prefix[k + 1] - prefix[i]
                    right = prefix[j + 1] - prefix[k + 1]
                    if left < right:
                        this_cost = score[k + 1][j] + remain[k + 1][j]
                        this_remain = remain[k + 1][j]
                    elif right < left:
                        this_cost = score[i][k] + remain[i][k]
                        this_remain = remain[i][k]
                    else:
                        cost_l = score[i][k] + remain[i][k]
                        cost_r = score[k + 1][j] + remain[k + 1][j]
                        this_cost = min(cost_l, cost_r)
                        if cost_l <= cost_r:
                            this_remain = remain[i][k]
                        else:
                            this_remain = remain[k + 1][j]
                    if this_cost < min_cost:
                        min_cost = this_cost
                        best_remain = this_remain
                total = prefix[j + 1] - prefix[i]
                score[i][j] = total - min_cost
                remain[i][j] = best_remain
        return score[0][n - 1]
