class Solution:
    def minSwaps(self, s):
        n = len(s)
        even_ones = 0
        odd_ones = 0
        for i, c in enumerate(s):
            if c == '1':
                if i % 2 == 0:
                    even_ones += 1
                else:
                    odd_ones += 1
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        total_ones = even_ones + odd_ones
        mismatches_start0 = even_ones + (odd_positions - odd_ones)
        mismatches_start1 = (even_positions - even_ones) + odd_ones
        possible_start0 = total_ones == odd_positions
        possible_start1 = total_ones == even_positions
        if not possible_start0 and not possible_start1:
            return -1
        if possible_start0 and possible_start1:
            return min(mismatches_start0, mismatches_start1) // 2
        elif possible_start0:
            return mismatches_start0 // 2
        else:
            return mismatches_start1 // 2
