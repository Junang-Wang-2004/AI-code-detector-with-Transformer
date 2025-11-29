# Time:  O(n^2)
# Space: O(n)
# dp, kmp algorithm
class Solution2(object):
    def deleteString(self, s):
        """
        """
        def getPrefix(pattern, start):
            prefix = [-1]*(len(pattern)-start)
            j = -1
            for i in range(1, len(pattern)-start):
                while j != -1 and pattern[start+j+1] != pattern[start+i]:
                    j = prefix[j]
                if pattern[start+j+1] == pattern[start+i]:
                    j += 1
                prefix[i] = j
            return prefix

        if all(x == s[0] for x in s):
            return len(s)
        dp = [1]*len(s)  # dp[i]: max operation count of s[i:]
        for i in reversed(range(len(s)-1)):
            prefix = getPrefix(s, i)  # prefix[j]+1: longest prefix suffix length of s[i:j+1]
            for j in range(1, len(prefix), 2):
                if 2*(prefix[j]+1) == j+1:
                    dp[i] = max(dp[i], dp[i+(prefix[j]+1)]+1)
        return dp[0]


