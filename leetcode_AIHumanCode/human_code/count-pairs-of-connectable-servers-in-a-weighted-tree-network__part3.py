# Time:  O(n^2)
# Space: O(n)
# bfs
class Solution3(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        """
        def bfs(u, p, dist):
            result = 0
            q = [(u, p, dist)]
            while q:
                new_q = []
                for u, p, dist in q:
                    if dist%signalSpeed == 0:
                        result += 1
                    for v, w in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u, dist+w))
                q = new_q
            return result
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = [0]*(len(edges)+1)
        for u in range(len(result)):
            curr = 0
            for v, w in adj[u]:
                cnt = bfs(v, u, w)
                result[u] += curr*cnt
                curr += cnt
        return result
