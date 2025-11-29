class Solution:
    def singleNumber(self, nums):
        result = 0
        for i in range(32):
            bit_count = sum((n >> i) & 1 for n in nums) % 3
            if bit_count == 1:
                result |= 1 << i
        return result
