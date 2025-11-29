class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        a, b = x - 1, y - 1
        if a > b:
            a, b = b, a
        res = [0] * n
        for i in range(n):
            res[0] += 2
            px = min(abs(i - a), abs(i - b) + 1)
            res[px] += 1
            py
