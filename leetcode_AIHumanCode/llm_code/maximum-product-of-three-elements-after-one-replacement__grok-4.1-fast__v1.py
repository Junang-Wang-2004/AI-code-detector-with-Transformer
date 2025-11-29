class Solution:
    def maxProduct(self, nums):
        mx1 = 0
        mx2 = 0
        for n in nums:
            v = abs(n)
            if v > mx1:
                mx2 = mx1
                mx1 = v
            elif v > mx2:
                mx2 = v
        return mx1 * mx2 * 100000
