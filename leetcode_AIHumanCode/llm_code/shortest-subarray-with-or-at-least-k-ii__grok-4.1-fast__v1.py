class Solution:
    def minimumSubarrayLength(self, nums, k):
        bit_counts = [0] * 32
        active_or = 0
        shortest = len(nums) + 1
        start_idx = 0
        n = len(nums)
        for end_idx in range(n):
            current = nums[end_idx]
            for pos in range(32):
                bit_mask = 1 << pos
                if current & bit_mask:
                    if bit_counts[pos] == 0:
                        active_or |= bit_mask
                    bit_counts[pos] += 1
            while start_idx <= end_idx and active_or >= k:
                shortest = min(shortest, end_idx - start_idx + 1)
                to_remove = nums[start_idx]
                for pos in range(32):
                    bit_mask = 1 << pos
                    if to_remove & bit_mask:
                        bit_counts[pos] -= 1
                        if bit_counts[pos] == 0:
                            active_or &= ~bit_mask
                start_idx += 1
        return shortest if shortest <= n else -1
