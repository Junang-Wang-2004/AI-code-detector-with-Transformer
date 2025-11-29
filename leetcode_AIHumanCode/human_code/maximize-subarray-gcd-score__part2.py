# Time:  O(n^2 + n * logr), r = max(nums)
# Space: O(1)
# number theory, brute force
class Solution2(object):
    def maxGCDScore(self, nums, k):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lower_bit(x):
            return x&-x

        result = 0
        for i in range(len(nums)):
            mn = float("inf")
            g = cnt = 0
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                bit = lower_bit(nums[j])
                if bit < mn:
                    mn = bit
                    cnt = 0
                if bit == mn:
                    cnt += 1
                result = max(result, g*(j-i+1)*(2 if cnt <= k else 1))
                if g*(len(nums)-i)*2 <= result:
                    break
        return result

