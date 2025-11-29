class Solution(object):
    def minimumOneBitOperations(self, n):
        ans = 0
        prev_bit = 0
        for pos in range(31, -1, -1):
            curr_bit = ((n >> pos) & 1) ^ prev_bit
            if curr_bit:
                ans |= (1 << pos)
            prev_bit = curr_bit
        return ans
