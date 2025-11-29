class Solution:
    def maxLength(self, ribbons, k):
        total = sum(ribbons)
        lo = 1
        hi = total // k
        while lo <= hi:
            mid = (lo + hi) // 2
            pieces = sum(r // mid for r in ribbons)
            if pieces >= k:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
