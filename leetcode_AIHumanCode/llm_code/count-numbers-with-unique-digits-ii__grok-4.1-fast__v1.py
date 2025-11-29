class Solution:
    def numberCount(self, a, b):
        def count(n):
            if n < 0:
                return 0
            s = str(n)
            L = len(s)
            from functools import lru_cache
            @lru_cache(None)
            def dfs(pos, mask, tight, leading):
                if pos == L:
                    return 1
                ans = 0
                up = int(s[pos]) if tight else 9
                for d in range(up + 1):
                    new_tight = 1 if tight and d == up else 0
                    if leading and d == 0:
                        ans += dfs(pos + 1, 0, new_tight, 1)
                        continue
                    new_leading = 0
                    if leading:
                        new_mask = 1 << d
                    else:
                        if mask & (1 << d):
                            continue
                        new_mask = mask | (1 << d)
                    ans += dfs(pos + 1, new_mask, new_tight, new_leading)
                return ans
            return dfs(0, 0, 1, 1)
        return count(b) - count(a - 1)
