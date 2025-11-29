class Solution:
    def minOperations(self, n):
        res = 0
        while n > 0:
            if n % 2 == 0:
                n //= 2
            else:
                res += 1
                half = n // 2
                n = half + (half % 2)
        return res
