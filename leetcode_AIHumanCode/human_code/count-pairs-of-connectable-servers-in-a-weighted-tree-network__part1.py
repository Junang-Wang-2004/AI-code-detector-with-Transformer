# Time:  O(n^2)
# Space: O(n)

# iterative dfs
class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        """
        def iter_dfs(u, p, dist):
            result = 0
            stk = [(u, p, dist)]
            while stk:
                u, p, dist = stk.pop()
                if dist%signalSpeed == 0:
                    result += 1
                for v, w in reversed(adj[u]):
                    if v == p:
                        continue
                    stk.append((v, u, dist+w))
            return result
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        result = [0]*(len(edges)+1)
        for u in range(len(result)):
            curr = 0
            for v, w in adj[u]:
                cnt = iter_dfs(v, u, w)
                result[u] += curr*cnt
                curr += cnt
        return result


