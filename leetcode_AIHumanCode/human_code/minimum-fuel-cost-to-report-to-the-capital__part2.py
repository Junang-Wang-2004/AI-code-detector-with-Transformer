# Time:  O(n)
# Space: O(h)
# dfs
class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        def dfs(u, p, d):
            cnt = 1+sum(dfs(v, u, d+1) for v in adj[u] if v != p)
            if d:
                result[0] += ceil_divide(cnt, seats)
            return cnt
    
        adj = [[] for _ in range(len(roads)+1)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1, 0)
        return result[0]
