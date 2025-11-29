class Solution:
    def commonFactors(self, a, b):
        x, y = a, b
        while y:
            x, y = y, x % y
        g = x
        cnt = 0
        for i in range(1, int(g ** 0.5) + 1):
            if g % i == 0:
                cnt += 1 if i * i == g else 2
        return cnt
