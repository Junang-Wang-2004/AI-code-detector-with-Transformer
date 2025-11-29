class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n < 3:
            return 1
        p, q, r = 0, 1, 1
        for _ in range(n - 2):
            s = p + q + r
            p, q, r = q, r, s
        return r
