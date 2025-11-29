class Solution:
    def reverseBits(self, n):
        val = 0
        for idx in range(32):
            if n & (1 << idx):
                val |= 1 << (31 - idx)
        return val
