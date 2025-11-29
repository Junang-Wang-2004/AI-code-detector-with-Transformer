class Solution(object):
    def maxProduct(self, nums):
        maximum = max(nums)
        mask_size = 1
        num_bits = 0
        while mask_size <= maximum:
            mask_size *= 2
            num_bits += 1
        array_size = 1 << num_bits
        subset_max = [0] * array_size
        for value in nums:
            subset_max[value] = value
        for current_bit in range(num_bits):
            bit_value = 1 << current_bit
            for current_mask in range(array_size):
                if (current_mask & bit_value) == 0:
                    mask_with_bit = current_mask | bit_value
                    subset_max[mask_with_bit] = max(subset_max[mask_with_bit], subset_max[current_mask])
        full_mask = array_size - 1
        max_prod = 0
        for partition in range(array_size):
            complement = full_mask ^ partition
            product = subset_max[partition] * subset_max[complement]
            if product > max_prod:
                max_prod = product
        return max_prod
