# Time:  O(n)
# Space: O(n)
# dfs
class Solution2(object):
    def placedCoins(self, edges, cost):
        """
        """
        def dfs(u, p):
            arr = [cost[u]]
            for v in adj[u]:
                if v == p:
                    continue
                arr.extend(dfs(v, u))
                arr.sort()
                if len(arr) > 5:
                    arr = arr[:2]+arr[-3:]
            result[u] = 1 if len(arr) < 3 else max(arr[0]*arr[1]*arr[-1], arr[-3]*arr[-2]*arr[-1], 0)
            return arr
                
        adj = [[] for _ in range(len(cost))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]*len(cost)
        dfs(0, -1)
        return result
