class Solution(object):
    def numOfSubsequences(self, s):
        total_t = s.count('T')
        # First pass: compute max L prefix * T suffix product
        max_lt_prod = 0
        prefix_l = 0
        suffix_t = total_t
        for char in s:
            max_lt_prod = max(max_lt_prod, prefix_l * suffix_t)
            if char == 'L':
                prefix_l += 1
            elif char == 'T':
                suffix_t -= 1
        # Second pass: compute LC, CT, LCT
        prefix_l = 0
        prefix_c = 0
        total_lc = 0
        total_ct = 0
        total_lct = 0
        for char in s:
            if char == 'L':
                prefix_l += 1
            elif char == 'C':
                total_lc += prefix_l
                prefix_c += 1
            else:
                total_ct += prefix_c
                total_lct += total_lc
        return total_lct + max(total_ct, max_lt_prod, total_lc)
