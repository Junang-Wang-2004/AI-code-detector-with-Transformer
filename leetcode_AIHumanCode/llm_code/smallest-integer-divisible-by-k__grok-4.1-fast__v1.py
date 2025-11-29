class Solution(object):
    def smallestRepunitDivByK(self, K):
        if K % 2 == 0 or K % 5 == 0:
            return -1
        accum = 0
        ten_pow = 1
        for length in range(1, K + 1):
            accum = (accum + ten_pow) % K
            if accum == 0:
                return length
            ten_pow = (ten_pow * 10) % K
        return -1
