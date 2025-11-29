class Solution:
    def waysToReachStair(self, k):
        def binom(n, r):
            if r < 0 or r > n:
                return 0
            if r > n - r:
                r = n - r
            res = 1
            for j in range(r):
                res = res * (n - j) // (j + 1)
            return res

        ans = 0
        height = 0
        while True:
            target = (1 << height) - k
            if target > height + 1:
                break
            ans += binom(height + 1, target)
            height += 1
        return ans
