class Solution:
    def countSubarrays(self, nums):
        ans = 0
        idx = 0
        sz = len(nums)
        while idx < sz:
            end = idx
            while end + 1 < sz and nums[end] < nums[end + 1]:
                end += 1
            seg_len = end - idx + 1
            ans += seg_len * (seg_len + 1) // 2
            idx = end + 1
        return ans
