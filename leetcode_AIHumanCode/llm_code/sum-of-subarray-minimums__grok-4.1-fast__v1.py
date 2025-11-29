class Solution:
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        n = len(A)
        prev_smaller = [-1] * n
        stk = []
        for i in range(n):
            while stk and A[stk[-1]] >= A[i]:
                stk.pop()
            prev_smaller[i] = stk[-1] if stk else -1
            stk.append(i)
        next_leq = [n] * n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and A[stk[-1]] > A[i]:
                stk.pop()
            next_leq[i] = stk[-1] if stk else n
            stk.append(i)
        total = 0
        for i in range(n):
            left_span = i - prev_smaller[i]
            right_span = next_leq[i] - i
            total = (total + A[i] * left_span * right_span) % MOD
        return total
