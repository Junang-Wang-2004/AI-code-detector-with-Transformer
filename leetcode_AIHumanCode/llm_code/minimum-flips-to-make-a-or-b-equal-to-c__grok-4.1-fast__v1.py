class Solution:
    def minFlips(self, a, b, c):
        flips = 0
        for pos in range(32):
            ba = (a >> pos) & 1
            bb = (b >> pos) & 1
            bc = (c >> pos) & 1
            if bc == 0:
                flips += ba + bb
            elif ba == 0 and bb == 0:
                flips += 1
        return flips
