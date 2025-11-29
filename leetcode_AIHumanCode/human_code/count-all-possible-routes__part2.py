# Time:  O(n^2 * f)
# Space: O(n * f)
class Solution2(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        """
        MOD = 10**9+7
        dp = [[0]*(fuel+1) for _ in range(len(locations))]
        dp[start][0] = 1
        for f in range(fuel+1):
            for i in range(len(locations)):
                for j in range(len(locations)):
                    if i == j:
                        continue
                    d = abs(locations[i]-locations[j])
                    if f-d < 0:
                        continue
                    dp[i][f] = (dp[i][f]+dp[j][f-d])%MOD
        return reduce(lambda x, y: (x+y)%MOD, dp[finish])
