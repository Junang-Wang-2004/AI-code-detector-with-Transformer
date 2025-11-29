class Solution(object):
    def assignBikes(self, workers, bikes):
        n = len(workers)
        N = 1 << n
        INF = 10**9 + 7
        dists = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dists[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        popcounts = [bin(m).count('1') for m in range(N)]
        dp = [INF] * N
        dp[0] = 0
        for mask in range(1, N):
            wrkr = popcounts[mask] - 1
            for bke in range(n):
                if mask & (1 << bke):
                    p_mask = mask ^ (1 << bke)
                    dp[mask] = min(dp[mask], dp[p_mask] + dists[wrkr][bke])
        result = [-1] * n
        mask = N - 1
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if mask & (1 << j):
                    p_mask = mask ^ (1 << j)
                    if dp[mask] == dp[p_mask] + dists[i][j]:
                        result[i] = j
                        mask = p_mask
                        break
        return result
