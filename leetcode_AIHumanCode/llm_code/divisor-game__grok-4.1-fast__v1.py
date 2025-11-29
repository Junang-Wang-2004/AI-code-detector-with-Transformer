class Solution:
    def divisorGame(self, n):
        iswin = [False] * (n + 1)
        for num in range(2, n + 1):
            iswin[num] = any(num % x == 0 and not iswin[num - x] for x in range(1, num))
        return iswin[n]
