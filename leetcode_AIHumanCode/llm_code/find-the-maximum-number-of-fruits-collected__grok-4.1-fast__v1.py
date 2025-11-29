class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        for x in range(n):
            l = x + 1
            r = n - x - 1
            if l < r:
                for y in range(l, r):
                    fruits[x][y] = 0
        for x in range(1, n - 1):
            for y in range(x + 1, n):
                a = fruits[x - 1][y - 1]
                b = fruits[x - 1][y]
                c = fruits[x - 1][y + 1] if y + 1 < n else 0
                fruits[x][y] += max(a, b, c)
        for y in range(n):
            t = y + 1
            b = n - y - 1
            if t < b:
                for x in range(t, b):
                    fruits[x][y] = 0
        for y in range(1, n - 1):
            for x in range(y + 1, n):
                a = fruits[x - 1][y - 1]
                b = fruits[x][y - 1]
                c = fruits[x + 1][y - 1] if x + 1 < n else 0
                fruits[x][y] += max(a, b, c)
        total = sum(fruits[k][k] for k in range(n)) + fruits[n - 2][n - 1] + fruits[n - 1][n - 2]
        return total
