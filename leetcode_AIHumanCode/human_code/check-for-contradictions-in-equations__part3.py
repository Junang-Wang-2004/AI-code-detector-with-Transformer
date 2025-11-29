# Time:  O(e + q)
# Space: O(n)
import collections
import itertools


# dfs
class Solution2(object):
    def checkContradictions(self, equations, values):
        """
        """
        def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
            return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

        def iter_dfs(adj, u, lookup):
            stk = [u]
            lookup[u] = 1.0
            while stk:
                u = stk.pop()
                for v, k in adj[u]:
                    if v in lookup:
                        if not isclose(lookup[v], lookup[u]*k):
                            return True
                        continue
                    lookup[v] = lookup[u]*k
                    stk.append(v)
            return False

        adj = collections.defaultdict(set)
        for (a, b), k in zip(equations, values):
            adj[a].add((b, 1.0/k))
            adj[b].add((a, 1.0*k))
        lookup = {}
        for u in adj.keys():
            if u in lookup:
                continue
            if iter_dfs(adj, u, lookup):
                return True
        return False
