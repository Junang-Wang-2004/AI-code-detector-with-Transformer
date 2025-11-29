# Time:  O(n) ~ O(n^2), worst case in star tree 
# Space: O(n)
import collections


# memoization
class Solution3(object):
    def rootCount(self, edges, guesses, k):
        """
        """
        cnt = [0]
        def memoization(u, p):
            if (u, p) not in memo:
                memo[u, p] = int((p, u) in lookup)
                for v in adj[u]:
                    if v == p:
                        continue
                    cnt[0] += 1
                    memo[u, p] += memoization(v, u)
            return memo[u, p]

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = {(u, v) for u, v in guesses}
        memo = {}
        return sum(memoization(i, -1) >= k for i in adj.keys())
