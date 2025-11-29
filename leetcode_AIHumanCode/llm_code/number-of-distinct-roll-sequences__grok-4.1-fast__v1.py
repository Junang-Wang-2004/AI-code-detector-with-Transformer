class Solution:
    def distinctSequences(self, n):
        if n == 1:
            return 6
        MOD = 10**9 + 7
        def compute_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        N = 6
        graph = [[0] * N for _ in range(N)]
        for u in range(N):
            for v in range(N):
                if u != v and compute_gcd(u + 1, v + 1) == 1:
                    graph[u][v] = 1
        ways = [[0] * N for _ in range(N)]
        for prev in range(N):
            for cur in range(N):
                ways[prev][cur] = graph[prev][cur]
        for _ in range(n - 2):
            nxt_ways = [[0] * N for _ in range(N)]
            for p_prev in range(N):
                for p_cur in range(N):
                    cnt = ways[p_prev][p_cur]
                    if cnt == 0:
                        continue
                    for p_nxt in range(N):
                        if graph[p_cur][p_nxt] == 1 and p_prev != p_nxt:
                            nxt_ways[p_cur][p_nxt] = (nxt_ways[p_cur][p_nxt] + cnt) % MOD
            ways = nxt_ways
        res = 0
        for row in ways:
            for val in row:
                res = (res + val) % MOD
        return res
