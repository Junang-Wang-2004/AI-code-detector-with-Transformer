class Solution(object):
    def minMoves(self, nums, limit):
        num_pairs = len(nums) // 2
        max_t = 2 * limit + 2
        range_diff = [0] * (max_t + 1)
        match_bonus = [0] * (max_t + 1)
        length = len(nums)
        for idx in range(num_pairs):
            val1 = nums[idx]
            val2 = nums[length - 1 - idx]
            small = min(val1, val2)
            large = max(val1, val2)
            begin = small + 1
            finish = large + limit
            range_diff[begin] += 1
            if finish + 1 <= max_t:
                range_diff[finish + 1] -= 1
            total_sum = val1 + val2
            if total_sum <= max_t:
                match_bonus[total_sum] += 1
        accum_coverage = 0
        best_reuse = 0
        for target in range(2, 2 * limit + 1):
            accum_coverage += range_diff[target]
            current_reuse = accum_coverage + match_bonus[target]
            if current_reuse > best_reuse:
                best_reuse = current_reuse
        return 2 * num_pairs - best_reuse
