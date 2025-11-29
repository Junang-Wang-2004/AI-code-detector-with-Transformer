class Solution:
    def sumIndicesWithKSetBits(self, nums, k):
        length = len(nums)
        total_sum = 0
        
        def build_comb( bit_pos, bits_left, current_index ):
            nonlocal total_sum
            if bits_left == 0:
                if current_index < length:
                    total_sum += nums[current_index]
                return
            for pos in range(bit_pos, 32):
                next_index = current_index | (1 << pos)
                if next_index >= length:
                    break
                build_comb(pos + 1, bits_left - 1, next_index)
        
        build_comb(0, k, 0)
        return total_sum
