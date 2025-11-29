import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        MOD = 10**9 + 7
        n = len(nums1)
        prefix = sorted(nums1)
        presum = sum(abs(nums1[k] - nums2[k]) for k in range(n)) % MOD
        best_reduction = 0
        for idx in range(n):
            tgt = nums2[idx]
            curr_diff = abs(nums1[idx] - tgt)
            pos = bisect.bisect_left(prefix, tgt)
            closest = float('inf')
            if pos < n:
                closest = min(closest, abs(prefix[pos] - tgt))
            if pos > 0:
                closest = min(closest, abs(prefix[pos - 1] - tgt))
            reduction = curr_diff - closest
            if reduction > best_reduction:
                best_reduction = reduction
        return (presum - best_reduction) % MOD
