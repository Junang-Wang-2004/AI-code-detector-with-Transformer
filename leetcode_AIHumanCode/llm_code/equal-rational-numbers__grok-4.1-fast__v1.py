class Solution(object):
    def isRationalEqual(self, S, T):
        def to_fraction(val):
            if '.' not in val:
                return int(val), 1
            whole, frac_part = val.split('.')
            whole_val = int(whole) if whole else 0
            if '(' not in frac_part:
                flen = len(frac_part)
                frac_num = int(frac_part) if frac_part else 0
                denom = 10 ** flen
            else:
                pre_rep_end = frac_part.index('(')
                pre_rep = frac_part[:pre_rep_end]
                pre_len = len(pre_rep)
                rep_end = frac_part.index(')', pre_rep_end)
                rep_seq = frac_part[pre_rep_end + 1:rep_end]
                rep_len = len(rep_seq)
                pre_num = int(pre_rep) if pre_rep else 0
                rep_num = int(rep_seq)
                rep_denom = 10 ** rep_len - 1
                frac_num = pre_num * rep_denom + rep_num
                denom = 10 ** pre_len * rep_denom
            return whole_val * denom + frac_num, denom

        num1, den1 = to_fraction(S)
        num2, den2 = to_fraction(T)
        return num1 * den2 == num2 * den1
