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
        for i in range(maxLength+1):
            dp[i%w] = 1 if i == 0 else 0
            if i-oneGroup >= 0:
                dp[i%w] = (dp[i%w]+dp[(i-oneGroup)%w])%MOD
            if i-zeroGroup >= 0:
                dp[i%w] = (dp[i%w]+dp[(i-zeroGroup)%w])%MOD
            if i >= minLength:
                result = (result+dp[i%w])%MOD
        return result


