class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 4:
            return [0, 1, 2, 6, 7][n]
        rem = n % 4
        if rem == 3:
            return n - 1
        return n + 1 + (1 if rem else 0)
