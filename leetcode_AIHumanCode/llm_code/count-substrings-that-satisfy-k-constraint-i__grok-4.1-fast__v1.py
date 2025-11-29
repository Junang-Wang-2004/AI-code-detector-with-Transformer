class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (s[i] == '1')
        total = 0
        for end in range(n):
            l, h = 0, end + 1
            while l < h:
                m = (l + h) // 2
                num_ones = pref[end + 1] - pref[m]
                win_len = end - m + 1
                num_zeros = win_len - num_ones
                if num_ones <= k or num_zeros <= k:
                    h = m
                else:
                    l = m + 1
            total += end - l + 1
        return total
