# Time:  O(|V| * |E|)
# Space: O(|V| + |E|)

# dfs
class Solution(object):
    def getAncestors(self, n, edges):
        """
        """
        def iter_dfs(adj, i, result):
            lookup = [False]*len(adj)
            stk = [i]
            while stk:
                u = stk.pop()
                for v in reversed(adj[u]):
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    stk.append(v)
                    result[v].append(i)
                    
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        result = [[] for _ in range(n)]
        for u in range(n):
            iter_dfs(adj, u, result)
        return result


