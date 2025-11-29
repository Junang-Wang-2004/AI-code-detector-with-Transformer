# Time:  O(n + m)
# Space: O(n + m)

# iterative dfs, tree diameter
class Solution(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//2
    
        def tree_diameter(edges):
            def iter_dfs():
                result = 0
                stk = [(1, (0, -1, [0]))]
                while stk:
                    step, args = stk.pop()
                    if step == 1:
                        u, p, ret = args
                        for v in reversed(adj[u]):
                            if v == p:
                                continue
                            ret2 = [0]
                            stk.append((2, (ret2, ret)))
                            stk.append((1, (v, u, ret2)))
                    elif step == 2:
                        ret2, ret = args
                        result = max(result, ret[0]+(ret2[0]+1))
                        ret[0] = max(ret[0], ret2[0]+1)
                return result
            
            adj = [[] for _ in range(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return iter_dfs()
        
        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)
        return max(ceil_divide(d1, 2)+1+ceil_divide(d2, 2), d1, d2)
        

