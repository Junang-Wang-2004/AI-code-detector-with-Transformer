# Time:  O(t^2)
# Space: O(t^2)
class Solution3(object):
    def largestNumber(self, cost, target):
        """
        """
        dp = [0]
        for t in range(1, target+1):
            dp.append(-1)
            for i, c in enumerate(cost):
                if t-c < 0:
                    continue
                dp[t] = max(dp[t], dp[t-c]*10 + i+1)
        return str(max(dp[t], 0))
