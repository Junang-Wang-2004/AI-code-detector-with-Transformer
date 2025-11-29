class Solution:
    def goodBinaryStrings(self, minLength, maxLength, oneGroup, zeroGroup):
        MOD = 10**9 + 7
        ans = 0
        if minLength == 0:
            ans = 1
        mx = maxLength
        end_zeros = [0] * (mx + 1)
        end_ones = [0] * (mx + 1)
        if oneGroup <= mx:
            end_ones[oneGroup] = 1
        if zeroGroup <= mx:
            end_zeros[zeroGroup] = 1
        for ln in range(1, mx + 1):
            if ln >= zeroGroup:
                end_zeros[ln] = (end_zeros[ln] + end_ones[ln - zeroGroup]) % MOD
            if ln >= oneGroup:
                end_ones[ln] = (end_ones[ln] + end_zeros[ln - oneGroup]) % MOD
        for ln in range(max(minLength, 1), mx + 1):
            ans = (ans + end_zeros[ln] + end_ones[ln]) % MOD
        return ans
