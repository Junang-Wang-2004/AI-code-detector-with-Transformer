class Solution(object):
    def maxValueAfterReverse(self, nums):
        total = 0
        best_minval = float('-inf')
        worst_maxval = float('inf')
        bonus = 0
        first, last = nums[0], nums[-1]
        m = len(nums)
        for k in range(m - 1):
            total += abs(nums[k] - nums[k + 1])
            lo = min(nums[k], nums[k + 1])
            hi = max(nums[k], nums[k + 1])
            best_minval = max(best_minval, lo)
            worst_maxval = min(worst_maxval, hi)
        for k in range(1, m):
            delta = abs(nums[k - 1] - nums[k])
            bonus = max(bonus, abs(first - nums[k]) - delta)
            bonus = max(bonus, abs(last - nums[k - 1]) - delta)
        swap_gain = 2 * (best_minval - worst_maxval)
        return total + max(bonus, swap_gain)
