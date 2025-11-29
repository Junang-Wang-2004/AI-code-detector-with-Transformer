# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
# dfs solution
class Solution3(object):
    def validPath(self, n, edges, start, end):
        """
        """
        def dfs(adj, start, target):
            stk = [start]
            lookup = set(stk)
            while stk:
                pos = stk.pop()
                if pos == target:
                    return True
                for nei in reversed(adj[pos]):
                    if nei in lookup:
                        continue
                    lookup.add(nei)
                    stk.append(nei)
            return False 

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return dfs(adj, start, end)
