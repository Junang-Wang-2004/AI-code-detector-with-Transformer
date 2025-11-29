# Time:  O(n ^ 2^n)
# Space: O(2^n)
# bitmasks, dp
class Solution2(object):
    def findMinimumTime(self, strength, K):
        """
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        def popcount(x):
            return bin(x).count('1')
    
        dp = [float('inf')]*(1<<len(strength))
        dp[0] = 0
        for mask in range(1, len(dp)):
            x = 1+(popcount(mask)-1)*K
            for i in range(len(strength)):
                if not (mask&(1<<i)):
                    continue
                dp[mask] = min(dp[mask], dp[mask^(1<<i)]+ceil_divide(strength[i], x))
        return dp[-1]
