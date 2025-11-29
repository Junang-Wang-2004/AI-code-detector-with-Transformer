# Time:  O(n^2 + q * n)
# Space: O(n^2)
# bfs
class Solution4(object):
    def closestNode(self, n, edges, query):
        """
        """
        def bfs(adj, root):
            dist = [len(adj)]*len(adj)
            q = [root]
            dist[root] = 0
            d = 0
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if d+1 >= dist[v]:
                            continue
                        dist[v] = d+1
                        new_q.append(v)
                q = new_q
                d += 1
            return dist

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v), adj[v].append(u)
        dist = [bfs(adj, i) for i in range(n)]
        result = []
        for start, end, node in query:
            x = end
            while start != end:
                if dist[node][start] < dist[node][x]:
                    x = start
                start = next(u for u in adj[start] if dist[u][end] < dist[start][end])
            result.append(x)
        return result


