class Solution:
    def smallestNumber(self, num):
        if num == 0:
            return 0
        s = str(abs(num))
        is_positive = num > 0
        digit_list = list(s)
        zero_count = digit_list.count('0')
        nz_digits = [d for d in digit_list if d != '0']
        if is_positive:
            nz_digits.sort()
            lead_digit = nz_digits[0]
            tail_digits = ['0'] * zero_count + nz_digits[1:]
        else:
            nz_digits.sort(reverse=True)
            lead_digit = nz_digits[0]
            tail_digits = nz_digits[1:] + ['0'] * zero_count
        num_str = lead_digit + ''.join(tail_digits)
        return (1 if is_positive else -1) * int(num_str)
