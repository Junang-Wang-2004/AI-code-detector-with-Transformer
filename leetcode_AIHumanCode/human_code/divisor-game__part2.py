# Time:  O(nlogn)
# Space: O(nlogn)
# dp, number theory
class Solution2(object):
    def divisorGame(self, n):
        """
        """
        def factors(n):
            result = [[] for _ in range(n+1)]
            for i in range(1, n+1):
                for j in range(i, n+1, i):
                    result[j].append(i)
            return result

        FACTORS = factors(n)
        dp = [False]*(n+1)
        for i in range(2, n+1):
            dp[i] = any(not dp[i-j] for j in FACTORS[i] if j != i)
        return dp[-1]


