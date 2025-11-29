# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

# dp
class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = 0
        dp = collections.Counter()
        for x in nums:
            new_dp = collections.Counter()
            if x%k == 0:
                dp[x] += 1
                for g, cnt in dp.items():
                    new_dp[gcd(g, x)] += cnt
            dp = new_dp
            result += dp[k]
        return result


