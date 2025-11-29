class Solution:
    def minOrAfterOperations(self, nums, k):
        if not nums:
            return 0
        highest_bit = max(nums).bit_length()
        ones_mask = (1 << highest_bit) - 1
        val = 0
        for position in range(highest_bit - 1, -1, -1):
            val <<= 1
            accum = ones_mask
            req_ops = 0
            for element in nums:
                accum &= element >> position
                if accum & ~val:
                    req_ops += 1
                else:
                    accum = ones_mask
            if req_ops > k:
                val |= 1
        return val
