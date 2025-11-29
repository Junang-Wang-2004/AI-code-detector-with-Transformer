class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        base = arr[0]
        delta = (arr[-1] - base) // n
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] != base + delta * m:
                r = m
            else:
                l = m + 1
        return base + delta * l
