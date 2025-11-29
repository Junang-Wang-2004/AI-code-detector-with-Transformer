class Solution:
    def maxTargetNodes(self, edges1, edges2, k):
        def build_adj(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def ball_counts(adj, max_k):
            n = len(adj)
            if max_k < 0:
                return [0] * n
            kk = min(max_k, n - 1)
            sub_dp = [[0] * (kk + 1) for _ in range(n)]

            def dfs_down(node, par):
                sub_dp[node][0] = 1
                for nxt in adj[node]:
                    if nxt != par:
                        dfs_down(nxt, node)
                        for dist in range(kk):
                            sub_dp[node][dist + 1] += sub_dp[nxt][dist]

            dfs_down(0, -1)

            res = [0] * n

            def dfs_up(node, par, ext_counts):
                sz = sum(sub_dp[node][d] + ext_counts[d] for d in range(kk + 1))
                res[node] = sz
                for nxt in adj[node]:
                    if nxt == par:
                        continue
                    new_ext = [0] * (kk + 1)
                    for d in range(kk):
                        subtr = sub_dp[nxt][d - 1] if d > 0 else 0
                        side = sub_dp[node][d] - subtr
                        new_ext[d + 1] = ext_counts[d] + side
                    dfs_up(nxt, node, new_ext)

            zero_ext = [0] * (kk + 1)
            dfs_up(0, -1, zero_ext)
            return res

        tree2_adj = build_adj(edges2)
        tree2_balls = ball_counts(tree2_adj, k - 1)
        max_tree2 = max(tree2_balls)

        tree1_adj = build_adj(edges1)
        tree1_balls = ball_counts(tree1_adj, k)

        return [tree1_balls[i] + max_tree2 for i in range(len(tree1_balls))]
