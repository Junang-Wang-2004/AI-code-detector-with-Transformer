from functools import reduce
# Time:  O(n^2 * k)
# Space: O(k)
# knapsack dp, combinatorics
class Solution_TLE(object):
    def kInversePairs(self, n, k):
        """
        """
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for i in range(n):
            dp = [reduce(lambda total, k: (total+dp[j-k])%MOD, range(min(i+1, j+1)), 0) for j in range(len(dp))]
        return dp[-1]%MOD


class Solution_ConstructPermutation(object):
    def kInversePairs(self, n, k):
        """
        """
        MOD = 10**9+7
        dp = [[] for _ in range(k+1)]
        dp[0].append([])
        for i in range(n):
            dp = [[[x+int(x >= i-k) for x in p]+[i-k] for k in range(min(i+1, j+1)) for p in dp[j-k]] for j in range(len(dp))]
        assert(all(sum(int(p[j] > p[i]) for i in range(n) for j in range(i)) == len(dp)-1) for p in dp[-1])
        return len(dp[-1])%MOD


class Solution_ConstructPermutation2(object):
    def kInversePairs(self, n, k):
        """
        """
        MOD = 10**9+7
        dp = [[] for _ in range(k+1)]
        dp[0].append([])
        for i in range(n):
            dp = [[p[:len(p)-k]+[i]+p[len(p)-k:] for k in range(min(i+1, j+1)) for p in dp[j-k]] for j in range(len(dp))]
        assert(all(sum(int(p[j] > p[i]) for i in range(n) for j in range(i)) == len(dp)-1) for p in dp[-1])
        return len(dp[-1])%MOD
