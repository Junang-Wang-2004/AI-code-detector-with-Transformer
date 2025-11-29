class Solution(object):
    def minLargest(self, nums1, nums2):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        par_long = [x % 2 for x in nums1]
        par_short = [x % 2 for x in nums2]
        len_long, len_short = len(par_long), len(par_short)
        prev_dp = [float('inf')] * (len_short + 1)
        prev_dp[0] = 0
        for k in range(1, len_short + 1):
            cost = prev_dp[k - 1]
            delta = 2 if cost % 2 == par_short[k - 1] else 1
            prev_dp[k] = cost + delta
        for idx in range(1, len_long + 1):
            curr_dp = [float('inf')] * (len_short + 1)
            for k in range(len_short + 1):
                cost_up = prev_dp[k]
                delta_up = 2 if cost_up % 2 == par_long[idx - 1] else 1
                curr_dp[k] = cost_up + delta_up
                if k > 0:
                    cost_left = curr_dp[k - 1]
                    delta_left = 2 if cost_left % 2 == par_short[k - 1] else 1
                    curr_dp[k] = min(curr_dp[k], cost_left + delta_left)
            prev_dp = curr_dp
        return prev_dp[len_short]
