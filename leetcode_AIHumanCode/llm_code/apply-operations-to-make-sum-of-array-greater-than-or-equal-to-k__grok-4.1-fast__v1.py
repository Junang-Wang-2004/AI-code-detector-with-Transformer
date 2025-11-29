class Solution:
    def minOperations(self, k):
        l, r = 0, k
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= k:
                l = mid + 1
            else:
                r = mid - 1
        root = r
        width = (k + root - 1) // root
        return root + width - 2
