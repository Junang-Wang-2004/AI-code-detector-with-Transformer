# Time:  O(n + m)
# Space: O(n + m)
# dfs, tree diameter
class Solution2(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//2
    
        def tree_diameter(edges):
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
        
        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)
        return max(ceil_divide(d1, 2)+1+ceil_divide(d2, 2), d1, d2)


