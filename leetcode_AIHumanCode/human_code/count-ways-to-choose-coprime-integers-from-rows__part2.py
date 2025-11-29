# Time:  O(n * m * rlogr)
# Space: O(r)
import collections


# dp, number thoery
class Solution2(object):
    def countCoprime(self, mat):
        """
        """
        MOD = 10**9+7
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        dp = collections.defaultdict(int)
        dp[0] = 1
        for row in mat:
            new_dp = collections.defaultdict(int)
            for x in row:
                for g, c in dp.items():
                    ng = gcd(g, x)
                    new_dp[ng] = (new_dp[ng]+c)%MOD
            dp = new_dp
        return dp[1]
