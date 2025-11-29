class Solution(object):
    def countBinaryPalindromes(self, n):
        if n == 0:
            return 1
        L = n.bit_length()
        cnt = 1
        for sz in range(1, L):
            ch = (sz + 1) // 2
            cnt += 1 << (ch - 1)
        hl = L // 2
        pre = n >> hl
        chl = L - hl
        minpre = 1 << (chl - 1)
        cnt += pre - minpre
        lhval = pre >> (chl - hl)
        revsuf = 0
        for j in range(hl):
            if lhval & (1 << j):
                revsuf |= 1 << (hl - 1 - j)
        mirr = (pre << hl) | revsuf
        if mirr <= n:
            cnt += 1
        return cnt
