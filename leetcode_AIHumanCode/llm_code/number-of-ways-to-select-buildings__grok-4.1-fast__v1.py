class Solution:
    def numberOfWays(self, s):
        cnt1_0 = cnt1_1 = cnt2_0 = cnt2_1 = cnt3_0 = cnt3_1 = 0
        for ch in s:
            typ = int(ch)
            if typ == 0:
                cnt1_0 += 1
                cnt2_0 += cnt1_1
                cnt3_0 += cnt2_1
            else:
                cnt1_1 += 1
                cnt2_1 += cnt1_0
                cnt3_1 += cnt2_0
        return cnt3_0 + cnt3_1
