# Time:  O(nlogn + r^2), r = max(rewardValues)
# Space: O(r)
# sort, dp
class Solution4(object):
    def maxTotalReward(self, rewardValues):
        """
        """
        dp = [False]*((max(rewardValues)*2-1)+1)
        dp[0] = True
        for v in sorted(set(rewardValues)):
            for x in range(v):
                dp[x+v] |= dp[x]
        return next(x for x in reversed(range(len(dp))) if dp[x])
