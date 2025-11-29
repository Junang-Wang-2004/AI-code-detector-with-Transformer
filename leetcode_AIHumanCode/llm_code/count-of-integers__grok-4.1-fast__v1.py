from functools import lru_cache

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        def numbers_up_to(s: str, lower: int, upper: int) -> int:
            if int(s) < 0:
                return 0
            digs = tuple(int(ch) for ch in s)
            length = len(digs)

            @lru_cache(None)
            def rec(position: int, total: int, constrained: bool) -> int:
                if position == length:
                    return 1 if lower <= total <= upper else 0
                res = 0
                limit = digs[position] if constrained else 9
                for choice in range(limit + 1):
                    next_total = total + choice
                    if next_total > upper:
                        continue
                    next_constrained = constrained and (choice == limit)
                    res = (res + rec(position + 1, next_total, next_constrained)) % MOD
                return res

            return rec(0, 0, True)

        prev = str(int(num1) - 1)
        result = (numbers_up_to(num2, min_sum, max_sum) - numbers_up_to(prev, min_sum, max_sum) + MOD) % MOD
        return result
