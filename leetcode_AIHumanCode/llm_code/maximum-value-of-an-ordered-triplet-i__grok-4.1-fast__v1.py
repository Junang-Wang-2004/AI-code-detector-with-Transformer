class Solution(object):
    def maximumTripletValue(self, nums):
        if len(nums) < 3:
            return 0
        score = 0
        prev1, prev2 = nums[0], nums[1]
        peak = max(prev1, prev2)
        gap = prev1 - prev2
        for pos in range(2, len(nums)):
            here = nums[pos]
            score = max(score, gap * here)
            gap = max(gap, peak - here)
            peak = max(peak, here)
        return score
