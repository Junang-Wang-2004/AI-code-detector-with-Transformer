# Time:  O(n^2 * 2^n)
# Space: O(n * 2^n)
# bfs based dp
class Solution2(object):
    def maximumCost(self, n, highways, k):
        """
        """
        if k+1 > n:  # required to optimize, otherwise, TLE or MLE
            return -1
        adj = [[] for _ in range(n)]
        for c1, c2, t in highways:
            adj[c1].append((c2, t))
            adj[c2].append((c1, t))
        result = -1
        dp = [(u, 1<<u, 0) for u in range(n)]
        while dp:
            new_dp = []
            for u, mask, total in dp:
                if bin(mask).count('1') == k+1:
                    result = max(result, total)
                for v, t in adj[u]:
                    if mask&(1<<v) == 0:
                        new_dp.append((v, mask|(1<<v), total+t))
            dp = new_dp
        return result
