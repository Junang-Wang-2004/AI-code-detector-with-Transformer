class Solution(object):
    def maxXorSubsequences(self, nums):
        if not nums:
            return 0
        max_bits = max(n.bit_length() for n in nums)
        bs = [0] * max_bits
        for val in nums:
            temp = val
            for idx in range(max_bits - 1, -1, -1):
                if bs[idx] and (temp & (1 << idx)):
                    temp ^= bs[idx]
            if temp:
                hi_bit = temp.bit_length() - 1
                bs[hi_bit] = temp
        maximum = 0
        for idx in range(max_bits - 1, -1, -1):
            if (maximum ^ bs[idx]) > maximum:
                maximum ^= bs[idx]
        return maximum
