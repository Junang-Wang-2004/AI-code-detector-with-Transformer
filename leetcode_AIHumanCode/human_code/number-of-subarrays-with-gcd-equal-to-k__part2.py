# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def subarrayGCD(self, nums, k):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = 0
        for i in range(len(nums)):
            g = 0
            for j in range(i, len(nums)):
                if nums[j]%k:
                    break
                g = gcd(g, nums[j])
                result += int(g == k)
        return result
