# Time:  O(nlogk + n * sqrt(k))
# Space: O(sqrt(k)), number of factors of k is at most sqrt(k)
import collections


# math, number theory
class Solution2(object):
    def countPairs(self, nums, k):
        """
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x

        result = 0
        gcds = collections.Counter()
        for x in nums:
            gcd_i = gcd(x, k)
            result += sum(cnt for gcd_j, cnt in gcds.items() if gcd_i*gcd_j%k == 0)
            gcds[gcd_i] += 1
        return result
