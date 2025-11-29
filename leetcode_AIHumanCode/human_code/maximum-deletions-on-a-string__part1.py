# Time:  O(n^2)
# Space: O(n)

# dp
class Solution(object):
    def deleteString(self, s):
        """
        """
        if all(x == s[0] for x in s):
            return len(s)
        dp2 = [[0]*(len(s)+1) for i in range(2)]  # dp2[i%2][j]: max prefix length of s[i:] and s[j:]
        dp = [1]*len(s)  # dp[i]: max operation count of s[i:]
        for i in reversed(range(len(s)-1)):
            for j in range(i+1, len(s)):
                dp2[i%2][j] = dp2[(i+1)%2][j+1]+1 if s[j] == s[i] else 0
                if dp2[i%2][j] >= j-i:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[0]


