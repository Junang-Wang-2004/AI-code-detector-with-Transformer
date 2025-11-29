# Time:  O(n * sqrt(k) * logk)
# Space: O(sqrt(k))

import collections


# dp
class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a//gcd(a, b)*b

        result = 0
        dp = collections.Counter()
        for x in nums:
            new_dp = collections.Counter()
            if k%x == 0:
                dp[x] += 1
                for l, cnt in dp.items():
                    new_dp[lcm(l, x)] += cnt
            dp = new_dp
            result += dp[k]
        return result


