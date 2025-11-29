# Time:  O(nlogn + r^2), r = max(rewardValues)
# Space: O(r)
# sort, dp
class Solution3(object):
    def maxTotalReward(self, rewardValues):
        """
        """
        mx = max(rewardValues)
        dp = [False]*((mx-1)+1)
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in range(min(v, mx-v)):
                dp[x+v] |= dp[x]
        return mx+next(x for x in reversed(range(len(dp))) if dp[x])


