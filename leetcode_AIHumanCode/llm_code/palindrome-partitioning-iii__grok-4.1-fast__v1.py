class Solution(object):
    def palindromePartition(self, s, k):
        n = len(s)
        INF = 10**9
        cost = [[0] * n for _ in range(n)]
        for start in range(n - 1):
            cost[start][start + 1] = 0 if s[start] == s[start + 1] else 1
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                inner_cost = cost[start + 1][end - 1]
                cost[start][end] = inner_cost if s[start] == s[end] else inner_cost + 1
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for num_parts in range(1, k + 1):
            for prefix_len in range(num_parts, n + 1):
                for prev_end in range(num_parts - 1, prefix_len):
                    prev_cost = dp[num_parts - 1][prev_end]
                    if prev_cost < INF:
                        add = cost[prev_end][prefix_len - 1]
                        dp[num_parts][prefix_len] = min(dp[num_parts][prefix_len], prev_cost + add)
        return dp[k][n]
