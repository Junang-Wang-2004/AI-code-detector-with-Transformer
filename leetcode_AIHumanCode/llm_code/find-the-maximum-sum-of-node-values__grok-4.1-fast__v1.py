class Solution:
    def maximumValueSum(self, nums, k, edges):
        max_total = 0
        flip_parity = 0
        least_adjust = float('inf')
        for num in nums:
            flipped = num ^ k
            if flipped > num:
                max_total += flipped
                flip_parity = 1 - flip_parity
            else:
                max_total += num
            least_adjust = min(least_adjust, abs(num - flipped))
        if flip_parity:
            max_total -= least_adjust
        return max_total
