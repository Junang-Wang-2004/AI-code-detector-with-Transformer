class Solution:
    def minBitwiseArray(self, nums):
        result = []
        for val in nums:
            if val % 2 == 0:
                result.append(-1)
                continue
            trailing_ones = 0
            temp_val = val
            while temp_val % 2 == 1:
                trailing_ones += 1
                temp_val //= 2
            subtract = 1 << (trailing_ones - 1)
            result.append(val - subtract)
        return result
