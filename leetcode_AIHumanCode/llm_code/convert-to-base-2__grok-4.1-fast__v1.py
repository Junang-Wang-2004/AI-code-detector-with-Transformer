class Solution:
    def baseNeg2(self, n):
        s = ''
        while n:
            r = n % 2
            s = str(r) + s
            n = (n - r) // -2
        return s or '0'
