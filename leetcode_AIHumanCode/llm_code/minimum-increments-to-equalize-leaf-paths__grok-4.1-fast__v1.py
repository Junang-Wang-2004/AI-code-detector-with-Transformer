class Solution:
    def minIncrease(self, n, edges, cost):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        sum_cnt = [0]
        def dfs(cur, parent):
            ch_heights = []
            for nxt in adj[cur]:
                if nxt != parent:
                    ch_heights.append(dfs(nxt, cur))
            if ch_heights:
                mh = max(ch_heights)
                sum_cnt[0] += ch_heights.count(mh)
                return cost[cur] + mh
            return cost[cur]
        dfs(0, -1)
        return n - 1 - sum_cnt[0]
