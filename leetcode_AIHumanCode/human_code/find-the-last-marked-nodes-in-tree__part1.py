# Time:  O(n)
# Space: O(n)

# bfs
class Solution(object):
    def lastMarkedNodes(self, edges):
        """
        """
        def bfs(root):
            new_root = -1
            dist = [-1]*len(adj)
            dist[root] = 0
            q = [root]
            while q:
                new_root = q[0]
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if dist[v] != -1:
                            continue
                        dist[v] = dist[u]+1
                        new_q.append(v)
                q = new_q
            return dist, new_root
            
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        _, u = bfs(0)
        dist1, v = bfs(u)
        dist2, _ = bfs(v)
        return [u if dist1[w] > dist2[w] else v for w in range(len(adj))]


