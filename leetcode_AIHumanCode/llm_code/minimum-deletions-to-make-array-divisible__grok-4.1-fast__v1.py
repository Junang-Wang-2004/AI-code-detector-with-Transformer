class Solution:
    def minOperations(self, nums, numsDivide):
        def gcd(p, q):
            while q:
                p, q = q, p % q
            return p
        
        if not numsDivide:
            return -1
        
        gd = numsDivide[0]
        for v in numsDivide[1:]:
            gd = gcd(gd, v)
            if gd == 1:
                break
        
        nums.sort()
        for i, val in enumerate(nums):
            if gd % val == 0:
                return i
        return -1
