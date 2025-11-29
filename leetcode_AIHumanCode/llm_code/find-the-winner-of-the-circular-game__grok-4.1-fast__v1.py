class Solution:
    def findTheWinner(self, n, k):
        pos = 0
        for size in range(2, n + 1):
            pos = (pos + k) % size
        return pos + 1
