# Time:  O(n) 
# Space: O(h)

import collections


# iterative dfs
class Solution(object):
    def rootCount(self, edges, guesses, k):
        """
        """
        def iter_dfs():
            result = 0
            stk = [(0, -1)]
            while stk:
                u, p = stk.pop()
                result += int((p, u) in lookup)
                for v in adj[u]:
                    if v == p:
                        continue
                    stk.append((v, u))
            return result
        
        def iter_dfs2(curr):
            result = 0
            stk = [(0, -1, curr)]
            while stk:
                u, p, curr = stk.pop()
                if (p, u) in lookup:
                    curr -= 1
                if (u, p) in lookup:
                    curr += 1
                result += int(curr >= k)
                for v in adj[u]:
                    if v == p:
                        continue
                    stk.append((v, u, curr))
            return result

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = {(u, v) for u, v in guesses}
        curr = iter_dfs()
        return iter_dfs2(curr)


