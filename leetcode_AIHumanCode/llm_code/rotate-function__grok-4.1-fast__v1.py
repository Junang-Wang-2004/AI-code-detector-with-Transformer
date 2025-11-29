class Solution(object):
    def maxRotateFunction(self, A):
        n = len(A)
        total = 0
        f = 0
        for i in range(n):
            total += A[i]
            f += i * A[i]
        ans = f
        for k in range(1, n + 1):
            prev_end = A[n - k]
            f += total - n * prev_end
            ans = max(ans, f)
        return ans
