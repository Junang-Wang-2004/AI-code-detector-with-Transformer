class Solution:
    def findNumber(self):
        num_bits = 30
        bit_values = [commonBits(1 << i) for i in range(num_bits)]
        prev_values = [commonBits(0)] + bit_values[:-1]
        return sum((1 << i) for i, (current, prior) in enumerate(zip(bit_values, prev_values)) if current - prior == 1)
