# Time:  O(n)
# Space: O(n)
# bfs
class Solution3(object):
    def lastMarkedNodes(self, edges):
        """
        """
        def increase(x):
            return (x[0]+1, x[1])

        def topological_traversal():
            p = [-2]*len(adj)
            p[0] = -1
            topological_order = [0]
            for u in topological_order:
                for v in reversed(adj[u]):
                    if p[v] != -2:
                        continue
                    p[v] = u
                    topological_order.append(v)
            dp = [[(0, u)]*2 for u in range(len(adj))]
            for u in reversed(topological_order):
                for v in adj[u]:
                    if v == p[u]:
                        continue
                    curr = increase(dp[v][0])
                    for i in range(len(dp[u])):
                        if curr > dp[u][i]:
                            curr, dp[u][i] = dp[u][i], curr
            return dp

        def bfs():
            result = [-1]*len(adj)
            q = [(0, -1, (0, -1))]
            while q:
                new_q = []
                for u, p, curr in q:
                    result[u] = max(dp[u][0], curr)[1]
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u, increase(max(dp[u][dp[u][0][1] == dp[v][0][1]], curr))))
                q = new_q
            return result

        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = topological_traversal()
        return bfs()


