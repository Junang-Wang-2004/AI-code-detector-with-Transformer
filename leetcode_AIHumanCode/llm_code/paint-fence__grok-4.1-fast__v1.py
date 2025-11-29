class Solution:
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        prev2 = k
        prev1 = k * k
        for i in range(3, n + 1):
            curr = (k - 1) * (prev2 + prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
