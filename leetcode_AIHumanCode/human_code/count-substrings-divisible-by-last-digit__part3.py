# Time:  O(d^2 * n)
# Space: O(d^2)
# dp
class Solution3(object):
    def countSubstrings(self, s):
        """
        """
        result = 0
        dp = [[0]*10 for _ in range(10)]
        for i in range(1, len(s)+1):
            new_dp = [[0]*10 for _ in range(10)]
            x = ord(s[i-1])-ord('0')
            for d in range(1, 9+1):
                new_dp[d][x%d] += 1
                for r in range(d):
                    new_dp[d][(r*10+x)%d] += dp[d][r]
            dp = new_dp
            result += dp[x][0]
        return result
