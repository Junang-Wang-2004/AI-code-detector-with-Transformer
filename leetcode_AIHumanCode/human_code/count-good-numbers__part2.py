# Time:  O(logn)
# Space: O(1)
class Solution2(object):
    def countGoodNumbers(self, n):
        """
        """
        MOD = 10**9 + 7
        return pow(5, (n+1)//2%(MOD-1), MOD)*pow(4, n//2%(MOD-1), MOD) % MOD
