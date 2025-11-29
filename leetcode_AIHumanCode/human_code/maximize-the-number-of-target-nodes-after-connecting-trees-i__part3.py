# Time:  O(n^2 + m^2)
# Space: O(n + m)
# brute force, bfs
class Solution3(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        """
        def bfs(u, adj, k):
            result = 0
            q = [(u, -1)]
            while q:
                if k == -1:
                    break
                k -= 1
                new_q = []
                result += len(q)
                for u, p in q:
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u))
                q = new_q
            return result
    
        def find_adj(edges):
            adj = [[] for _ in range(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        adj2 = find_adj(edges2)
        mx = max(bfs(u, adj2, k-1) for u in range(len(adj2)))
        adj1 = find_adj(edges1)
        return [mx+bfs(u, adj1, k) for u in range(len(adj1))]
