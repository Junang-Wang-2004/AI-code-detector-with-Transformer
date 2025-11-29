class Solution:
    def maximumPoints(self, edges, coins, k):
        n = len(coins)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        maxc = max(coins)
        D = maxc.bit_length() + 1
        def dfs(nd, pr):
            ch_dps = [dfs(v, nd) for v in adj[nd] if v != pr]
            res = [0] * (D + 1)
            for dep in range(D + 1):
                g1 = (coins[nd] >> dep) - k
                for cdp in ch_dps:
                    g1 += cdp[dep]
                g2 = (coins[nd] >> (dep + 1))
                for cdp in ch_dps:
                    g2 += cdp[dep + 1] if dep + 1 <= D else 0
                res[dep] = max(g1, g2)
            return res
        return dfs(0, -1)[0]
