class Solution:
    def reverse(self, x):
        if not x:
            return 0
        is_neg = x < 0
        if is_neg:
            x = -x
        limit = 2147483647
        rev = 0
        while x:
            d = x % 10
            x //= 10
            if rev > limit // 10 or (rev == limit // 10 and d > limit % 10):
                return 0
            rev = rev * 10 + d
        return -rev if is_neg else rev
