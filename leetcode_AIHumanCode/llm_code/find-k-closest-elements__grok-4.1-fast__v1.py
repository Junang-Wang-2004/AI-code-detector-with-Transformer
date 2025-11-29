class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        lo, hi = 0, n - k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]
