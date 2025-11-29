class Solution(object):
    def maximumTripletValue(self, nums):
        if len(nums) < 3:
            return 0
        outcome = 0
        peak = nums[0]
        opt_diff = peak - nums[1]
        peak = max(peak, nums[1])
        for num in nums[2:]:
            outcome = max(outcome, opt_diff * num)
            opt_diff = max(opt_diff, peak - num)
            peak = max(peak, num)
        return outcome
