class Solution(object):
    def addToArrayForm(self, A, K):
        digits = []
        pos = len(A) - 1
        while pos >= 0 or K > 0:
            if pos >= 0:
                total = A[pos] + K % 10
                K //= 10
            else:
                total = K % 10
                K //= 10
            digits.append(total % 10)
            K += total // 10
            if pos >= 0:
                pos -= 1
        digits.reverse()
        return digits
