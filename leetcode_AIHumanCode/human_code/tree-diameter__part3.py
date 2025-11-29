# Time:  O(|V| + |E|)
# Space: O(|E|)
# bfs, tree dp
class Solution3(object):
    def treeDiameter(self, edges):
        """
        """
        def bfs():
            result = 0
            dp = [0]*len(adj)
            degree = list(map(len, adj))
            q = [u for u in range(len(degree)) if degree[u] == 1]
            while q:
                new_q = []
                for u in q:
                    if degree[u] == 0:
                        continue
                    degree[u] -= 1
                    for v in adj[u]:
                        if degree[v] == 0:
                            continue
                        result = max(result, dp[v]+(dp[u]+1))
                        dp[v] = max(dp[v], (dp[u]+1))
                        degree[v] -= 1
                        if degree[v] == 1:
                            new_q.append(v)
                q = new_q
            return result
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bfs()


