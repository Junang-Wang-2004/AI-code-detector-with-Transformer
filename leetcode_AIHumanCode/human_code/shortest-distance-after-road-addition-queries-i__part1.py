# Time:  O(n^2)
# Space: O(n^2)

# bfs
class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        """
        def bfs(u, v):
            adj[u].append(v)
            q = [u]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if dist[u]+1 >= dist[v]:
                            continue
                        dist[v] = dist[u]+1
                        new_q.append(v)
                q = new_q
            return dist[-1]

        adj = [[] for _ in range(n)]
        for u in range(n-1):
            adj[u].append(u+1)
        dist = list(range(n))
        return [bfs(u, v) for u, v in queries]


