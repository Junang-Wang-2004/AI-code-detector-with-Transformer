class Solution(object):
    def concatHex36(self, n):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sq = n * n
        cu = sq * n
        hex_part = hex(sq)[2:].upper()
        base36_part = ""
        temp = cu
        while temp:
            base36_part = digits[temp % 36] + base36_part
            temp //= 36
        if not base36_part:
            base36_part = "0"
        return hex_part + base36_part
