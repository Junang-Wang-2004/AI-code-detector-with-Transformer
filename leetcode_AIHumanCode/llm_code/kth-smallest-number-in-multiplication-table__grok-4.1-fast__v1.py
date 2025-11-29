class Solution:
    def findKthNumber(self, m, n, k):
        def numbers_leq(val):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(n, val // i)
            return cnt

        low = 1
        high = m * n
        while low < high:
            pivot = (low + high) // 2
            if numbers_leq(pivot) >= k:
                high = pivot
            else:
                low = pivot + 1
        return low
