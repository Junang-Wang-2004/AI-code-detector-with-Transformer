class Solution:
    def fractionToDecimal(self, numer, denom):
        if numer == 0:
            return "0"
        is_neg = (numer < 0) ^ (denom < 0)
        n, d = abs(numer), abs(denom)
        output = [str(n // d)]
        r = n % d
        if r:
            output.append(".")
            pos_map = {}
            digit_list = []
            i = 0
            while r and r not in pos_map:
                pos_map[r] = i
                r *= 10
                digit_list.append(str(r // d))
                r %= d
                i += 1
            if r in pos_map:
                rep_start = pos_map[r]
                digit_list = digit_list[:rep_start] + ["("] + digit_list[rep_start:] + [")"]
            output.extend(digit_list)
        s = "".join(output)
        return "-" + s if is_neg else s
