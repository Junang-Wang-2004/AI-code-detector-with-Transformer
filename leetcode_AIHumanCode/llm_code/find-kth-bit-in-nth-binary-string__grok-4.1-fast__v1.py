class Solution(object):
    def findKthBit(self, n, k):
        parity = 0
        pos = k
        lev = n
        while lev > 1:
            half = 1 << (lev - 1)
            if pos == half:
                parity ^= 1
                break
            if pos > half:
                pos = (1 << lev) - pos
                parity ^= 1
            lev -= 1
        return '1' if parity & 1 else '0'
