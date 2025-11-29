# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def numOfWays(self, n):
        """
        """
        MOD = 10**9 + 7
        aba, abc = 6, 6
        for _ in range(n-1):
            aba, abc = (3*aba%MOD + 2*abc%MOD)%MOD, \
                       (2*abc%MOD + 2*aba%MOD)%MOD
        return (aba+abc)%MOD
