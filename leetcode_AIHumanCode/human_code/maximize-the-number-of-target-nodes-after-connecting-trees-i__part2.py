# Time:  O((n + m) * k)
# Space: O((n + m) * k)
# dfs, tree dp
class Solution2(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        """
        def tree_dp(adj, k):
            def dfs1(u, p):
                for v in adj[u]:
                    if v == p:
                        continue
                    dfs1(v, u)
                dp[u][0] += 1
                for v in adj[u]:
                    if v == p:
                        continue
                    for d in range(k):
                        dp[u][d+1] += dp[v][d]
            
            def dfs2(u, p, curr):
                def update(v, u, curr):
                    new_curr = [0]*len(curr)
                    for d in range(len(curr)-1):
                        new_curr[d+1] = curr[d]+(dp[u][d]-(dp[v][d-1] if d-1 >= 0 else 0))
                    return new_curr

                for v in adj[u]:
                    if v == p:
                        continue
                    dfs2(v, u, update(v, u, curr))
                result[u] = sum(dp[u][i]+curr[i] for i in range(len(curr)))

            result = [0]*len(adj)
            k = min(k, len(adj)-1)
            if k == -1:
                return result
            dp = [[0]*(k+1) for _ in range(len(adj))]
            dfs1(0, -1)
            dfs2(0, -1, [0]*(k+1))
            return result

        def find_adj(edges):
            adj = [[] for _ in range(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adj2 = find_adj(edges2)
        mx = max(tree_dp(adj2, k-1))
        adj1 = find_adj(edges1)
        return [mx+x for x in tree_dp(adj1, k)]


