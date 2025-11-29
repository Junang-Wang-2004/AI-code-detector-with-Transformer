# Time:  O(n)
# Space: O(n)
# dfs, tree dp
class Solution2(object):
    def maxScore(self, edges):
        """
        """
        def dfs(u):
            if not adj[u]:
                return (0, 0)
            children = [dfs(v) for v, _ in adj[u]]
            without_u = sum(max(with_v, without_v) for with_v, without_v in children)
            with_u = max(without_u-max(with_v, without_v)+(without_v+adj[u][i][1]) for i, (with_v, without_v) in enumerate(children))
            return (with_u, without_u)
            
        adj = [[] for _ in range(len(edges))]
        for i, (p, w) in enumerate(edges):
            if i == 0:
                continue
            adj[p].append((i, w))
        return max(dfs(0))
