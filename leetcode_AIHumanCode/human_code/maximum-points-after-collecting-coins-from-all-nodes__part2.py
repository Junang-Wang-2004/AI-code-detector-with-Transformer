# Time:  O(nlogr), r = max(coins)
# Space: O(nlogr)
# tree dp, memoization
class Solution2(object):
    def maximumPoints(self, edges, coins, k):
        """
        """
        def memoization(u, p, d):
            if d >= max_d:
                return 0
            if lookup[u][d] is None:
                lookup[u][d] = max(((coins[u]>>d)-k)+sum(memoization(v, u, d) for v in adj[u] if v != p),
                                    (coins[u]>>(d+1))+sum(memoization(v, u, d+1) for v in adj[u] if v != p))
            return lookup[u][d]

        adj = [[] for _ in range(len(coins))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        max_d = max(coins).bit_length()
        lookup = [[None]*max_d for _ in range(len(coins))]
        return memoization(0, -1, 0)
