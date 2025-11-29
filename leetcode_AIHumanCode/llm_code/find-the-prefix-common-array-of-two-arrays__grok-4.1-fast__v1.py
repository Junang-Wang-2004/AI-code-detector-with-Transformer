class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        pos_in_a = [0] * (n + 1)
        pos_in_b = [0] * (n + 1)
        for idx in range(n):
            pos_in_a[A[idx]] = idx
            pos_in_b[B[idx]] = idx
        increments = [0] * n
        for val in range(1, n + 1):
            latest = max(pos_in_a[val], pos_in_b[val])
            increments[latest] += 1
        output = []
        total = 0
        for idx in range(n):
            total += increments[idx]
            output.append(total)
        return output
