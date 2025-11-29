class Solution:
    def singleNumber(self, nums):
        xor_sum = 0
        for val in nums:
            xor_sum ^= val
        mask = 1
        while (xor_sum & mask) == 0:
            mask <<= 1
        one = 0
        two = 0
        for val in nums:
            if val & mask:
                one ^= val
            else:
                two ^= val
        return [one, two]
