class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        n = len(nums1)
        abs_diffs = sorted(abs(nums1[i] - nums2[i]) for i in range(n))[::-1]
        total_reduce = min(k1 + k2, sum(abs_diffs))
        def cost_to_cap(cap_val):
            s = 0
            for d in abs_diffs:
                s += max(0, d - cap_val)
            return s
        l, r = 0, abs_diffs[0] if abs_diffs else 0
        while l < r:
            m = l + (r - l) // 2
            if cost_to_cap(m) <= total_reduce:
                r = m
            else:
                l = m + 1
        cap_val = l
        used = cost_to_cap(cap_val)
        extra = total_reduce - used
        sq_sum = 0
        for i in range(n):
            fd = min(abs_diffs[i], cap_val)
            if i < extra:
                fd -= 1
            sq_sum += fd * fd
        return sq_sum
