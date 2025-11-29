class Solution:
    def maxPower(self, s):
        n = len(s)
        if n == 0:
            return 0
        best = 1
        start = 0
        for i in range(1, n):
            if s[i] != s[i - 1]:
                best = max(best, i - start)
                start = i
        return max(best, n - start)
