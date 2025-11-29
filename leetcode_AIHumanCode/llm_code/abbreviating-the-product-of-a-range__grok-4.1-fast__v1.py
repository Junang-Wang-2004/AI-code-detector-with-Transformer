import math

class Solution(object):
    def abbreviateProduct(self, left, right):
        p_len = s_len = 5
        modulus = 10 ** (p_len + s_len)
        remain = 1
        zcount = 0
        large = False
        for val in range(left, right + 1):
            remain *= val
            while remain % 10 == 0:
                remain //= 10
                zcount += 1
            if remain >= modulus:
                large = True
                remain %= modulus
        if not large:
            return f"{remain}e{zcount}"
        frac_part = 0.0
        for val in range(left, right + 1):
            frac_part = (frac_part + math.log10(val)) % 1
        sig = 10 ** frac_part
        head = int(sig * (10 ** (p_len - 1)))
        head_str = str(head)
        tail = remain % (10 ** s_len)
        tail_str = f"{tail:0{s_len}d}"
        return f"{head_str}...{tail_str}e{zcount}"
