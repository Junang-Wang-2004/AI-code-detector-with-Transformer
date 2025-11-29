# Time:  O(n)
# Space: O(h)
# dfs
class Solution2(object):
    def countGoodNodes(self, edges):
        """
        """
        def dfs(u, p):
            total = l = 0
            valid = True
            for v in adj[u]:
                if v == p:
                    continue
                cnt = dfs(v, u)
                total += cnt
                l += 1
                if l*cnt != total:
                    valid = False
            if valid:
                result[0] += 1
            return total+1
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]
