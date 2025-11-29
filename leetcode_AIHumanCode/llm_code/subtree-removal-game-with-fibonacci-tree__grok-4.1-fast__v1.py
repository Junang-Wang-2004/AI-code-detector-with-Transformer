class Solution:
    def findGameWinner(self, n):
        remainder = n % 6
        return remainder == 0 or remainder > 1
