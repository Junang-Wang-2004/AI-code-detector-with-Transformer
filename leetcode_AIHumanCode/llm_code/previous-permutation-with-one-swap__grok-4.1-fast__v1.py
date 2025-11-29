class Solution:
    def prevPermOpt1(self, A):
        n = len(A)
        k = n - 2
        while k >= 0:
            if A[k] > A[k + 1]:
                break
            k -= 1
        else:
            return A
        m = n - 1
        while A[m] >= A[k]:
            m -= 1
        while m > 0 and A[m - 1] == A[m]:
            m -= 1
        A[k], A[m] = A[m], A[k]
        return A
