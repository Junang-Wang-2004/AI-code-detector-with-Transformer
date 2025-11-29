# Time:  O(10^(l/2) * n * l), l = 5
# Space: O(l)
# dp
class Solution2(object):
    def countPalindromes(self, s):
        """
        """
        MOD = 10**9+7
        result = 0
        for i in range(10):
            for j in range(10):
                pattern = "%s%s*%s%s" % (i, j, j, i)
                dp = [0]*(5+1)
                dp[0] = 1
                for k in range(len(s)):
                    for l in reversed(range(5)):
                        if pattern[l] == '*' or pattern[l] == s[k]:
                            dp[l+1] = (dp[l+1]+dp[l])%MOD
                result = (result+dp[5])%MOD
        return result
