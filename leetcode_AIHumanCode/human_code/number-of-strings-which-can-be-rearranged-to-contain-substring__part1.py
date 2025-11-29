# Time:  O(logn)
# Space: O(1)

# combinatorics, principle of inclusion-exclusion
class Solution(object):
    def stringCount(self, n):
        """
        """
        MOD = 10**9+7
        return (pow(26, n, MOD)-
                (25+25+25+n)*pow(25, n-1, MOD)+      # no l, t, e, ee
                (24+24+24+n+n+0)*pow(24, n-1, MOD)-  # no l|t, l|e, t|e, l|ee, t|ee, e|ee
                (23+n+0+0)*pow(23, n-1, MOD))%MOD    # no l|t|e, l|t|ee, l|e|ee, t|e|ee


