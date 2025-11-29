class Solution(object):
    def minRemoval(self, nums, k):
        a = sorted(nums)
        n = len(a)
        ans = 0
        for i in range(n):
            target = k * a[i]
            lo = i
            hi = n - 1
            while lo <= hi:
                m = (lo + hi) // 2
                if a[m] <= target:
                    lo = m + 1
                else:
                    hi = m - 1
            farthest = hi
            if farthest >= i:
                ans = max(ans, farthest - i + 1)
        return n - ans
