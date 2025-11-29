class Solution:
    def countSubarrays(self, nums, minK, maxK):
        total = 0
        window_start = 0
        last_min_pos = -1
        last_max_pos = -1
        for pos, num in enumerate(nums):
            if num < minK or num > maxK:
                window_start = pos + 1
                last_min_pos = -1
                last_max_pos = -1
            if num == minK:
                last_min_pos = pos
            if num == maxK:
                last_max_pos = pos
            if last_min_pos >= 0 and last_max_pos >= 0:
                total += min(last_min_pos, last_max_pos) - window_start + 1
        return total
