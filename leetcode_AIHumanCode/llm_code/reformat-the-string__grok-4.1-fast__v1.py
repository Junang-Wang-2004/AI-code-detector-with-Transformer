class Solution:
    def reformat(self, s):
        chars_alpha = [ch for ch in s if ch.isalpha()]
        chars_digit = [ch for ch in s if ch.isdigit()]
        cnt_alpha = len(chars_alpha)
        cnt_digit = len(chars_digit)
        if abs(cnt_alpha - cnt_digit) > 1:
            return ""
        output = []
        idx_a = idx_d = 0
        if cnt_alpha >= cnt_digit:
            for _ in range(cnt_digit):
                output.append(chars_alpha[idx_a])
                idx_a += 1
                output.append(chars_digit[idx_d])
                idx_d += 1
            if idx_a < cnt_alpha:
                output.append(chars_alpha[idx_a])
        else:
            for _ in range(cnt_alpha):
                output.append(chars_digit[idx_d])
                idx_d += 1
                output.append(chars_alpha[idx_a])
                idx_a += 1
            if idx_d < cnt_digit:
                output.append(chars_digit[idx_d])
        return "".join(output)
