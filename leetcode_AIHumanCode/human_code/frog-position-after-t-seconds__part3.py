# Time:  O(n)
# Space: O(n)
# dfs solution with recursion with better precision
class Solution3(object):
    def frogPosition(self, n, edges, t, target):
        """
        """        
        def dfs(G, target, t, node, parent):
            if not t or not (len(G[node])-(parent != 0)):
                return int(node == target)
            result = 0
            for child in G[node]:
                if child == parent:
                    continue
                result = dfs(G, target, t-1, child, node)
                if result:
                    break
            return result*(len(G[node])-(parent != 0))
        
        G = collections.defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        choices = dfs(G, target, t, 1, 0)
        return 1.0/choices if choices else 0.0


