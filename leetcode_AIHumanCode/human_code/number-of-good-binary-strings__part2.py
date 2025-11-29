# Time:  O(n), n = maxLength
# Space: O(w), w = max(oneGroup, zeroGroup)+1
# dp
class Solution(object):
    def goodBinaryStrings(self, minLength, maxLength, oneGroup, zeroGroup):
        """
        """
        MOD = 10**9+7
        result = 0
        w = max(oneGroup, zeroGroup)+1
        dp = [0]*w
        dp[0] = 1
        for i in range(maxLength+1):
            if i >= minLength:
                result = (result+dp[i%w])%MOD
            if i+oneGroup <= maxLength:
                dp[(i+oneGroup)%w] = (dp[(i+oneGroup)%w]+dp[i%w])%MOD
            if i+zeroGroup <= maxLength:
                dp[(i+zeroGroup)%w] = (dp[(i+zeroGroup)%w]+dp[i%w])%MOD
            dp[i%w] = 0
        return result
