class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        total_ones = 0
        max_bonus = 0
        prior_group = 0
        idx = 0
        length = len(s)
        while idx < length:
            if s[idx] == '1':
                total_ones += 1
                idx += 1
                continue
            this_group = 0
            while idx < length and s[idx] == '0':
                this_group += 1
                idx += 1
            if prior_group > 0:
                max_bonus = max(max_bonus, prior_group + this_group)
            prior_group = this_group
        return total_ones + max_bonus
