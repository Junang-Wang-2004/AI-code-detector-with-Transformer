class Solution(object):
    def fractionAddition(self, expression):
        def greatest_common_divisor(p, q):
            p = abs(p)
            while q:
                p, q = q, p % q
            return p

        s = expression
        pos = 0
        length = len(s)
        tops = []
        bottoms = []
        while pos < length:
            multiplier = 1
            if s[pos] == '+':
                pos += 1
            elif s[pos] == '-':
                multiplier = -1
                pos += 1
            num_start = pos
            while pos < length and s[pos].isdigit():
                pos += 1
            top_val = int(s[num_start:pos]) * multiplier
            if pos < length and s[pos] == '/':
                pos += 1
            den_start = pos
            while pos < length and s[pos].isdigit():
                pos += 1
            bottom_val = int(s[den_start:pos])
            tops.append(top_val)
            bottoms.append(bottom_val)

        acc_top = 0
        acc_bottom = 1
        for idx in range(len(tops)):
            frac_top = tops[idx]
            frac_bottom = bottoms[idx]
            acc_top = acc_top * frac_bottom + frac_top * acc_bottom
            acc_bottom = acc_bottom * frac_bottom
            divisor = greatest_common_divisor(acc_top, acc_bottom)
            acc_top //= divisor
            acc_bottom //= divisor
        return f"{acc_top}/{acc_bottom}"
