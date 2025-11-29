class Solution:
    def maxSum(self, nums1, nums2):
        MOD = 10**9 + 7
        p, q = 0, 0
        buf1, buf2 = 0, 0
        res = 0
        while p < len(nums1) or q < len(nums2):
            val1 = nums1[p] if p < len(nums1) else float('inf')
            val2 = nums2[q] if q < len(nums2) else float('inf')
            if val1 < val2:
                buf1 += val1
                p += 1
            elif val2 < val1:
                buf2 += val2
                q += 1
            else:
                res = (res + max(buf1, buf2) + val1) % MOD
                buf1 = buf2 = 0
                p += 1
                q += 1
        return (res + max(buf1, buf2)) % MOD
