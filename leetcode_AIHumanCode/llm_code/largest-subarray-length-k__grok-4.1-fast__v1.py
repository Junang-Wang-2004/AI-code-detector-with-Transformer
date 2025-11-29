class Solution(object):
    def largestSubarray(self, nums, k):
        n = len(nums)
        res_end = k - 1
        cur = 1
        lim = n - k + 1
        while cur < lim:
            bs = res_end - k + 1
            p = 0
            while p < k and nums[bs + p] == nums[cur + p]:
                p += 1
            if p < k and nums[bs + p] >= nums[cur + p]:
                cur += p + 1
            else:
                res_end = cur + k - 1
                cur += p + 1
        return nums[res_end - k + 1: res_end + 1]
