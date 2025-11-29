# Time:  O(e + q * n), at most O(n^3 + q)
# Space: O(n^2)
# bfs solution
import collections
import itertools


class Solution2(object):
    def calcEquation(self, equations, values, queries):
        """
        """
        adj = collections.defaultdict(dict)
        for (a, b), k in zip(equations, values):
            adj[a][b] = k
            adj[b][a] = 1.0/k

        def bfs(adj, a, b, lookup):
            if a not in adj or b not in adj:
                return -1.0
            if (a, b) in lookup:
                return lookup[a, b]
            visited = {a}
            q = collections.deque([(a, 1.0)])
            while q:
                u, val = q.popleft()
                if u == b:
                    lookup[a, b] = val
                    return val
                for v, k in adj[u].items():
                    if v in visited:
                        continue                    
                    visited.add(v)
                    q.append((v, val*k))
            lookup[a, b] = -1.0
            return -1.0

        lookup = {}
        return [bfs(adj, a, b, lookup) for a, b in queries]


