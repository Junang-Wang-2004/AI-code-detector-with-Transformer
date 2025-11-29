class Solution:
    def repeatedStringMatch(self, A, B):
        n, m = len(A), len(B)
        times = (m + n - 1) // n
        S = A * times
        if B in S:
            return times
        S += A
        if B in S:
            return times + 1
        return -1
