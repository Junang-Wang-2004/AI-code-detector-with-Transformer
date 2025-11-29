# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp
class Solution(object):
    def maxScore(self, edges):
        """
        """
        def iter_dfs():
            result = [(0, 0) for _ in range(len(adj))]
            stk = [(1, 0)]
            while stk:
                step, u = stk.pop()
                if step == 1:
                    if not adj[u]:
                        continue
                    stk.append((2, u))
                    for v, _ in adj[u]:
                        stk.append((1, v))
                elif step == 2:
                    without_u = sum(max(result[v]) for v, w in adj[u])
                    with_u = max(without_u-max(result[v])+(result[v][1]+w) for v, w in adj[u])
                    result[u] = (with_u, without_u)
            return max(result[0])
            
        adj = [[] for _ in range(len(edges))]
        for i, (p, w) in enumerate(edges):
            if i == 0:
                continue
            adj[p].append((i, w))
        return iter_dfs()

    
