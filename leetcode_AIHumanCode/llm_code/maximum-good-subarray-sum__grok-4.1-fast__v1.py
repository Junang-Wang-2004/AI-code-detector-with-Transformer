class Solution(object):
    def maximumSubarraySum(self, nums, k):
        min_pref = {}
        psum = 0
        ans = float('-inf')
        for num in nums:
            if num not in min_pref:
                min_pref[num] = psum
            else:
                min_pref[num] = min(min_pref[num], psum)
            for delta in [-k, k]:
                start_val = num + delta
                if start_val in min_pref:
                    curr_ps = psum + num
                    this_sum = curr_ps - min_pref[start_val]
                    ans = max(ans, this_sum)
            psum += num
        return ans if ans != float('-inf') else 0
