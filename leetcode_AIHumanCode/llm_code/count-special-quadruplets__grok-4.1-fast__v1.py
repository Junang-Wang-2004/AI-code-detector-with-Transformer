import collections

class Solution:
    def countQuadruplets(self, nums):
        total = 0
        freq_map = collections.Counter()
        freq_map[nums[-1]] = 1
        length = len(nums)
        for idx_c in range(length - 2, 1, -1):
            sum_c = nums[idx_c]
            for idx_b in range(1, idx_c):
                partial_sum = sum_c + nums[idx_b]
                for idx_a in range(idx_b):
                    target_sum = partial_sum + nums[idx_a]
                    total += freq_map[target_sum]
            freq_map[nums[idx_c]] += 1
        return total
