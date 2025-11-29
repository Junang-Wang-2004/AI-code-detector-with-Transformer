class Solution(object):
    def encode(self, s):
        n = len(s)
        memo = {}
        def helper(start, stop):
            if stop - start <= 1:
                return s[start:stop]
            key = (start, stop)
            if key in memo:
                return memo[key]
            result = s[start:stop]
            for split in range(start + 1, stop):
                l_enc = helper(start, split)
                r_enc = helper(split, stop)
                cand = l_enc + r_enc
                if len(cand) < len(result):
                    result = cand
            substr_len = stop - start
            if substr_len > 1:
                prefix = [0] * substr_len
                pref_len = 0
                for idx in range(1, substr_len):
                    while pref_len > 0 and s[start + idx] != s[start + pref_len]:
                        pref_len = prefix[pref_len - 1]
                    if s[start + idx] == s[start + pref_len]:
                        pref_len += 1
                    prefix[idx] = pref_len
                cycle = substr_len - prefix[substr_len - 1]
                if cycle < substr_len and substr_len % cycle == 0:
                    unit_enc = helper(start, start + cycle)
                    count = substr_len // cycle
                    rep_enc = f"{count}[{unit_enc}]"
                    if len(rep_enc) < len(result):
                        result = rep_enc
            memo[key] = result
            return result
        return helper(0, n)
