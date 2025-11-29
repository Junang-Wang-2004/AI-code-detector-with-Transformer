# Time:  O(|V| + |E|)
# Space: O(|E|)
# dfs
class Solution2(object):
    def treeDiameter(self, edges):
        """
        """
        def dfs(u, p):
            mx = 0
            for v in adj[u]:
                if v == p:
                    continue
                curr = dfs(v, u)
                result[0] = max(result[0], mx+(curr+1))
                mx = max(mx, curr+1)
            return mx
            
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]


