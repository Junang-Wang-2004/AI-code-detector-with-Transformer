# Time:  O(n * r^2 * logr)
# Space: O(r^2)
import collections
from functools import reduce


# dp, number theory
class Solution2(object):
    def subsequencePairCount(self, nums):
        """
        """
        MOD = 10**9+7
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        dp = collections.defaultdict(int)
        dp[(0, 0)] = 1
        for x in nums:
            new_dp = collections.defaultdict(int)
            for (g1, g2), cnt in list(dp.items()):
                ng1, ng2 = gcd(g1, x), gcd(g2, x)
                new_dp[(g1, g2)] = (new_dp[(g1, g2)]+cnt)%MOD
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)]+cnt)%MOD
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)]+cnt)%MOD
            dp = new_dp
        return reduce(lambda accu, x: (accu+x)%MOD, (cnt for (g1, g2), cnt in dp.items() if g1 == g2 > 0), 0)


