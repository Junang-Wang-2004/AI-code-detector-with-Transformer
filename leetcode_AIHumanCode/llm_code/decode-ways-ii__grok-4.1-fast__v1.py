class Solution:
    def numDecodings(self, s):
        MOD = 1000000007
        n = len(s)
        if s[0] == '0':
            return 0
        prev_ways = 9 if s[0] == '*' else 1
        pp_ways = 1
        for i in range(1, n):
            curr = s[i]
            prev_c = s[i - 1]
            single_w = 9 if curr == '*' else (1 if curr != '0' else 0)
            pair_w = 0
            if prev_c == '1':
                pair_w = 9 if curr == '*' else 1
            elif prev_c == '2':
                pair_w = 6 if curr == '*' else (1 if curr <= '6' else 0)
            elif prev_c == '*':
                pair_w = 15 if curr == '*' else (2 if curr <= '6' else 1)
            curr_ways = (single_w * prev_ways + pair_w * pp_ways) % MOD
            pp_ways = prev_ways
            prev_ways = curr_ways
        return prev_ways
