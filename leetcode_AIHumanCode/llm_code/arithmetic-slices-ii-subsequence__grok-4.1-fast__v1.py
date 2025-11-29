class Solution:
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        total = 0
        counts = [{} for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                d = A[i] - A[j]
                prev_count = counts[j].get(d, 0)
                current_count = counts[i].get(d, 0) + prev_count + 1
                counts[i][d] = current_count
                total += prev_count
        return total
