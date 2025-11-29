# Time:  O(m * t * n^2)
# Space: O(t * n)
class Solution2(object):
    def minCost(self, houses, cost, m, n, target):
        """
        """
        dp = {(0, 0): 0}
        for i, p in enumerate(houses):
            new_dp = {}
            for nk in (range(1, n+1) if not p else [p]):
                for j, k in dp:
                    nj = j + (k != nk)
                    if nj > target:
                        continue
                    new_dp[nj, nk] = min(new_dp.get((nj, nk), float("inf")), dp[j, k] + (cost[i][nk-1] if nk != p else 0))
            dp = new_dp
        return min([dp[j, k] for j, k in dp if j == target] or [-1])
