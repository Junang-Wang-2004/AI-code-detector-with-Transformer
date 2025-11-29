class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - mid - 1 < k:
                lo = mid + 1
            else:
                hi = mid
        return k + lo
