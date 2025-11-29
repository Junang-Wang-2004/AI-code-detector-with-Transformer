from functools import lru_cache

class Solution:
    def countSteppingNumbers(self, low, high):
        MOD = 10**9 + 7
        def digit_dp(limit):
            s = str(limit)
            n = len(s)

            @lru_cache(None)
            def dfs(pos, tight, prev, leading):
                if pos == n:
                    return 1 if not leading else 0
                res = 0
                max_digit = int(s[pos]) if tight else 9
                for d in range(max_digit + 1):
                    new_tight = 1 if tight and d == max_digit else 0
                    if leading and d == 0:
                        res = (res + dfs(pos + 1, new_tight, -1, 1)) % MOD
                    else:
                        new_prev = d
                        if not leading and abs(d - prev) != 1:
                            continue
                        res = (res + dfs(pos + 1, new_tight, new_prev, 0)) % MOD
                return res

            return dfs(0, 1, -1, 1)

        return (digit_dp(high) - digit_dp(low - 1) + MOD) % MOD
