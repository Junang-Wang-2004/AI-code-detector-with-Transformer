# Time:  O(m * t * n^2)
# Space: O(t * n)

class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        """
        # dp[i][j][k]: cost of covering i+1 houses with j+1 neighbor groups and the (k+1)th color
        dp = [[[float("inf") for _ in range(n)] for _ in range(target)] for _ in range(2)]
        for i in range(m):
            dp[i%2] = [[float("inf") for _ in range(n)] for _ in range(target)]
            for j in range(min(target, i+1)):
                for k in range(n):
                    if houses[i] and houses[i]-1 != k:
                        continue
                    same = dp[(i-1)%2][j][k] if i-1 >= 0 else 0
                    diff = (min([dp[(i-1)%2][j-1][nk] for nk in range(n) if nk != k] or [float("inf")]) if j-1 >= 0 else float("inf")) if i-1 >= 0 else 0
                    paint = cost[i][k] if not houses[i] else 0
                    dp[i%2][j][k] = min(same, diff)+paint
        result = min(dp[(m-1)%2][-1])
        return result if result != float("inf") else -1


