class Solution:
    def numberOfUniqueGoodSubsequences(self, binary):
        MOD = 10**9 + 7
        cnt_zero_end = 0
        cnt_one_end = 0
        zero_present = False
        for ch in binary:
            prev_total = (cnt_zero_end + cnt_one_end) % MOD
            if ch == '0':
                cnt_zero_end = prev_total
                zero_present = True
            else:
                cnt_one_end = (prev_total + 1) % MOD
        return (cnt_zero_end + cnt_one_end + (1 if zero_present else 0)) % MOD
