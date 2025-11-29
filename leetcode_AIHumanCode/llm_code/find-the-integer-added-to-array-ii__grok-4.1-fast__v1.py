import collections

class Solution:
    def minimumAddedInteger(self, nums1, nums2):
        cnt_b = collections.Counter(nums2)
        max_b = max(nums2)
        s = sorted(nums1)
        cand1 = max_b - s[-1]
        cand2 = max_b - s[-2]
        cand3 = max_b - s[-3]
        for delta in [cand1, cand2, cand3]:
            cnt_a = collections.Counter(z + delta for z in nums1)
            if cnt_b <= cnt_a:
                return delta
