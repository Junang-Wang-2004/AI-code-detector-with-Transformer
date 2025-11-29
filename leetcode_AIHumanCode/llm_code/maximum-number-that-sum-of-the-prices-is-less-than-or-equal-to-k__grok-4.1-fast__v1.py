class Solution:
    def findMaximumNumber(self, k, x):
        def get_block_size(remaining, carry, x):
            current_cost = carry
            bit_pos = 0
            while True:
                extra = (1 << bit_pos) if (bit_pos + 1) % x == 0 else 0
                if (current_cost << 1) + extra > remaining:
                    return bit_pos, current_cost
                current_cost = (current_cost << 1) + extra
                bit_pos += 1

        n = 0
        carry = 0
        while k >= carry:
            block_len, block_cost = get_block_size(k, carry, x)
            k -= block_cost
            n |= (1 << block_len)
            if (block_len + 1) % x == 0:
                carry += 1
        return n - 1
