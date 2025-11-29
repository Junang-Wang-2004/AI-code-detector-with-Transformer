class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        x, y = 1, 1
        for i in range(3, n + 1):
            x, y = y, x + y
        return y
