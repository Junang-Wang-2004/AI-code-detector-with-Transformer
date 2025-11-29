class Solution:
    def minimumSplits(self, nums):
        def gcd(p, q):
            while p and q:
                p, q = q, p % q
            return p or q

        splits, cur = 0, 0
        for val in nums:
            temp_gcd = gcd(cur, val)
            if temp_gcd == 1:
                splits += 1
                cur = val
            else:
                cur = temp_gcd
        return splits + 1
