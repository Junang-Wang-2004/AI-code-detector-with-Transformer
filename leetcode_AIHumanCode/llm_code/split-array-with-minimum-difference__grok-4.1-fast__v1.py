class Solution(object):
    def splitArray(self, nums):
        n = len(nums)
        idx_l = 0
        while idx_l < n - 1 and nums[idx_l] < nums[idx_l + 1]:
            idx_l += 1
        pre_sum = 0
        for k in range(idx_l):
            pre_sum += nums[k]
        idx_r = n - 1
        while idx_r > 0 and nums[idx_r] < nums[idx_r - 1]:
            idx_r -= 1
        post_sum = 0
        for k in range(idx_r + 1, n):
            post_sum += nums[k]
        plat_size = idx_r - idx_l + 1
        if plat_size >= 3:
            return -1
        if plat_size == 2:
            return abs(pre_sum + nums[idx_l] - (nums[idx_r] + post_sum))
        return min(
            abs(pre_sum + nums[idx_l] - post_sum),
            abs(pre_sum - (nums[idx_l] + post_sum))
        )
