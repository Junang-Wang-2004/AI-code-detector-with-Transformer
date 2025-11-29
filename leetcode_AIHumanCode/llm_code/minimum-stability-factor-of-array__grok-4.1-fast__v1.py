from math import gcd

class Solution:
    def minStable(self, nums, maxC):
        n = len(nums)
        if n == 0:
            return 0
        logn = n.bit_length()
        sparse = [[0] * n for _ in range(logn)]
        for i in range(n):
            sparse[0][i] = nums[i]
        for lv in range(1, logn):
            pw = 1 << (lv - 1)
            for start in range(n - (1 << lv) + 1):
                sparse[lv][start] = gcd(sparse[lv - 1][start], sparse[lv - 1][start + pw])
        def get_gcd(lo, hi):
            sz = hi - lo + 1
            k = sz.bit_length() - 1
            pw = 1 << k
            return gcd(sparse[k][lo], sparse[k][hi - pw + 1])
        def valid_length(length):
            num_stable = 0
            cur = 0
            while cur + length <= n:
                if get_gcd(cur, cur + length - 1) >= 2:
                    num_stable += 1
                    cur += length
                else:
                    cur += 1
            return num_stable > maxC
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if valid_length(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
