class Solution(object):
    def largestPalindrome(self, num_digits, divisor):
        if divisor in (1, 3, 9):
            return '9' * num_digits
        elif divisor == 5:
            if num_digits <= 2:
                return '5' * num_digits
            return '5' + '9' * (num_digits - 2) + '5'
        elif divisor == 6:
            if num_digits <= 2:
                return '6' * num_digits
            if num_digits % 2:
                sec = num_digits // 2 - 1
                return '8' + '9' * sec + '8' + '9' * sec + '8'
            sec = num_digits // 2 - 2
            return '8' + '9' * sec + '77' + '9' * sec + '8'
        elif divisor in (2, 4, 8):
            adj = {2: 1, 4: 2, 8: 3}[divisor]
            tot_adj = 2 * adj
            if num_digits <= tot_adj:
                return '8' * num_digits
            return '8' * adj + '9' * (num_digits - tot_adj) + '8' * adj
        else:  # divisor == 7
            blk_sz = 6
            full = num_digits // (2 * blk_sz)
            rem = num_digits % (2 * blk_sz)
            pref = '999999' * full
            midd = self._build_mod7_pal(rem)
            return pref + midd + pref

    def _build_mod7_pal(self, sz):
        if sz == 0:
            return ''
        digs = ['9'] * sz
        hf = sz // 2
        for d in range(9, -1, -1):
            tmp = digs[:]
            tmp[hf] = chr(48 + d)
            if sz % 2 == 0:
                tmp[hf - 1] = chr(48 + d)
            val = 0
            for cc in tmp:
                val = (val * 10 + (ord(cc) - 48)) % 7
            if val == 0:
                return ''.join(tmp)
        return ''
