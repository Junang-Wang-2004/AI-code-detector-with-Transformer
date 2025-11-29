# Time:  O(n^2)
# Space: O(n)
# dfs
class Solution2(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        """
        def dfs(u, p, dist):
            cnt = 1 if dist%signalSpeed == 0 else 0
            for v, w in adj[u]:
                if v == p:
                    continue
                cnt += dfs(v, u, dist+w)
            return cnt
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = [0]*(len(edges)+1)
        for u in range(len(result)):
            curr = 0
            for v, w in adj[u]:
                cnt = dfs(v, u, w)
                result[u] += curr*cnt
                curr += cnt
        return result


