class Solution:
    def kthLuckyNumber(self, k):
        n = k + 1
        s = ""
        while n > 1:
            s = ("7" if n % 2 else "4") + s
            n //= 2
        return s
