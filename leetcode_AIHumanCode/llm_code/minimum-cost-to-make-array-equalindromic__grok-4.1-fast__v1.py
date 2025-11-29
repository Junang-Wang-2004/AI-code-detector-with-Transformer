class Solution:
    def minimumCost(self, nums):
        def compute_median(arr):
            s = sorted(arr)
            sz = len(s)
            m = sz // 2
            if sz % 2:
                return s[m]
            return (s[m - 1] + s[m]) // 2

        def generate_palindromes(val):
            s_val = str(val)
            l_val = len(s_val)
            pals_set = set()
            pals_set.add(10 ** l_val + 1)
            pals_set.add(10 ** (l_val - 1) - 1)
            h_len = (l_val + 1) // 2
            pref_num = int(s_val[:h_len])
            for adj in (-1, 0, 1):
                pref_adj = pref_num + adj
                if pref_adj <= 0:
                    continue
                pref_s = str(pref_adj)
                rev_s = pref_s[:-1][::-1] if l_val % 2 else pref_s[::-1]
                pal_num = int(pref_s + rev_s)
                pals_set.add(pal_num)
            return pals_set

        med_val = compute_median(nums)
        pal_candidates = generate_palindromes(med_val)

        def calc_cost(tgt):
            return sum(abs(x - tgt) for x in nums)

        return min(calc_cost(p) for p in pal_candidates)
