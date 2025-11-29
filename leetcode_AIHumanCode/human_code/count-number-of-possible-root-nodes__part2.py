# Time:  O(n) 
# Space: O(h)
import collections


# dfs
class Solution2(object):
    def rootCount(self, edges, guesses, k):
        """
        """
        def dfs(u, p):
            cnt = int((p, u) in lookup)
            for v in adj[u]:
                if v == p:
                    continue
                cnt += dfs(v, u)
            return cnt
        
        def dfs2(u, p, curr):
            if (p, u) in lookup:
                curr -= 1
            if (u, p) in lookup:
                curr += 1
            cnt = int(curr >= k)
            for v in adj[u]:
                if v == p:
                    continue
                cnt += dfs2(v, u, curr)
            return cnt

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = {(u, v) for u, v in guesses}
        curr = dfs(0, -1)
        return dfs2(0, -1, curr)


