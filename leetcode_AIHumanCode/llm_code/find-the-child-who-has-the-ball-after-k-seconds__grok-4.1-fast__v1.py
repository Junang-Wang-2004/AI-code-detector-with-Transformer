class Solution(object):
    def numberOfChild(self, n, k):
        m = n - 1
        p = 2 * m
        s = k % p
        return s if s <= m else p - s
