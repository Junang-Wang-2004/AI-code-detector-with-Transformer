class Solution:
    def maxSubarraySum(self, nums):
        if not nums:
            return 0
        best = float('-inf')
        pref = 0
        lo = 0
        lo_plain = 0
        mins_at_val = {}
        for v in nums:
            pref += v
            best = max(best, pref - lo)
            if v < 0:
                old = mins_at_val.get(v, float('inf'))
                cand = min(old, lo_plain) + v
                mins_at_val[v] = cand
                lo = min(lo, cand)
            lo_plain = min(lo_plain, pref)
            lo = min(lo, lo_plain)
        return best
