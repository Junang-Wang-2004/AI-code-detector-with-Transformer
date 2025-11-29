import bisect
from itertools import permutations

class Solution:
    def nextBeautifulNumber(self, n):
        beautiful = []
        for mask in range(1, 1 << 9):
            chars = []
            clen = 0
            for dig in range(1, 10):
                if mask & (1 << (dig - 1)):
                    chars.extend([str(dig)] * dig)
                    clen += dig
            if clen > 7 or clen == 0:
                continue
            uniq_perms = set(permutations(chars))
            for perm in uniq_perms:
                num = int(''.join(perm))
                beautiful.append(num)
        beautiful = sorted(set(beautiful))
        pos = bisect.bisect_right(beautiful, n)
        return beautiful[pos]
