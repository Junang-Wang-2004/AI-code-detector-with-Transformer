class Solution(object):
    def beautifulSubstrings(self, s, k):
        vow_set = set('aeiou')
        n = len(s)
        bal_pref = [0] * (n + 1)
        for j in range(n):
            bal_pref[j + 1] = bal_pref[j] + (1 if s[j] in vow_set else -1)
        
        modd = 1
        k_temp = k
        d = 2
        while d * d <= k_temp:
            exp_cnt = 0
            while k_temp % d == 0:
                k_temp //= d
                exp_cnt += 1
            if exp_cnt > 0:
                expo = (exp_cnt + 1) // 2 + (1 if d == 2 else 0)
                modd *= d ** expo
            d += 1
        if k_temp > 1:
            expo = 1 + (1 if k_temp == 2 else 0)
            modd *= k_temp ** expo
        
        freq_dict = {}
        total = 0
        for idx in range(n + 1):
            curr_bal = bal_pref[idx]
            curr_mod = idx % modd
            keyy = (curr_bal, curr_mod)
            total += freq_dict.get(keyy, 0)
            freq_dict[keyy] = freq_dict.get(keyy, 0) + 1
        return total
