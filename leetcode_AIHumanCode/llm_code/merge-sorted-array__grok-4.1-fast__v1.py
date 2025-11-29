class Solution(object):
    def merge(self, A, m, B, n):
        p = m - 1
        q = n - 1
        k = m + n - 1
        while p >= 0 or q >= 0:
            if q < 0:
                A[k] = A[p]
                p -= 1
            elif p < 0:
                A[k] = B[q]
                q -= 1
            elif A[p] > B[q]:
                A[k] = A[p]
                p -= 1
            else:
                A[k] = B[q]
                q -= 1
            k -= 1
