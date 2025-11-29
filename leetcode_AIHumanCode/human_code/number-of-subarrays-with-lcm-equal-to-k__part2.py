# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
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
        for i in range(len(nums)):
            l = 1
            for j in range(i, len(nums)):
                if k%nums[j]:
                    break
                l = lcm(l, nums[j])
                result += int(l == k)
        return result
