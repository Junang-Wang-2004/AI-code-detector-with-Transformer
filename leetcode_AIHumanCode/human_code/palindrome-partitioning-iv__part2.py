# Time:  O(n^2)
# Space: O(n^2)
class Solution2(object):
    def checkPartitioning(self, s):
        """
        """        
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        for i in range(1, len(s)-1):
            if not dp[0][i-1]:
                continue
            for j in range(i+1, len(s)):
                if not dp[j][-1]:
                    continue
                if dp[i][j-1]:
                    return True
        return False
