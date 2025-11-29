from collections import Counter
from bisect import bisect_left, bisect_right

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        n = len(nums)
        freq_map = Counter(nums)
        unique_vals = sorted(freq_map)
        answer = 0
        # Compute max coverage for potential new targets
        start = 0
        max_coverage = 0
        for end in range(n):
            while nums[end] - nums[start] > 2 * k:
                start += 1
            max_coverage = max(max_coverage, end - start + 1)
        answer = max(answer, min(max_coverage, numOperations))
        # Compute for existing targets
        for target_val in unique_vals:
            low_bound = bisect_left(nums, target_val - k)
            high_bound = bisect_right(nums, target_val + k) - 1
            win_len = high_bound - low_bound + 1 if low_bound <= high_bound else 0
            orig_freq = freq_map[target_val]
            extra_possible = win_len - orig_freq
            answer = max(answer, orig_freq + min(extra_possible, numOperations))
        return answer
